from rest_framework import viewsets

from .models import Contact, Tag, ContactTag
from .serializers import ContactSerializer, TagSerializer, ContactTagSerializer


# Contact API
class ContactAPI(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class TagAPI(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ContactTagAPI(viewsets.ModelViewSet):
    queryset = ContactTag.objects.all()
    serializer_class = ContactTagSerializer
