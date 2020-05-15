from rest_framework import serializers

from .models import Contact, Tag, ContactTag


# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ContactTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTag
        fields = "__all__"
