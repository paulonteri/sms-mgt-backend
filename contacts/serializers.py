from rest_framework import serializers

from .models import Contact, Tag, ContactTag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ContactTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTag
        fields = "__all__"


# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    tags = ContactTagSerializer(source='contacttag_set', many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ["id", "first_name", "last_name", "other_name", "phone_number", "email",
                  "gender", "is_active", "time_added",
                  "time_last_edited", "tags"]
