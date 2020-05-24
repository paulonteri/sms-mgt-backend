from rest_framework import serializers

from .models import Contact, Tag, ContactTag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(TagSerializer, self).create(validated_data)


class ContactTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTag
        fields = "__all__"

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(ContactTagSerializer, self).create(validated_data)


class ContactTagLessDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTag
        fields = ["id", "tag"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(ContactTagLessDetailedSerializer, self).create(validated_data)

    # Contact Serializer


class ContactSerializer(serializers.ModelSerializer):
    tags = ContactTagLessDetailedSerializer(source='contacttag_set', many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ["id", "first_name", "last_name", "other_name", "phone_number", "email",
                  "gender", "is_active", "time_added",
                  "time_last_edited", "tags"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(ContactSerializer, self).create(validated_data)
