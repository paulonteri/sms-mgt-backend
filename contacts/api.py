import json

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Contact, Tag, ContactTag
from .serializers import ContactSerializer, TagSerializer, ContactTagSerializer


class TagAPI(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ContactTagAPI(viewsets.ModelViewSet):
    queryset = ContactTag.objects.all()
    serializer_class = ContactTagSerializer


# Contact API
class ContactAPI(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    tags = None

    def create(self, request, *args, **kwargs):
        # get tags
        try:
            self.tags = json.loads(request.data.__getitem__("tags"))
        except Exception:
            pass
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # get contact
        instance = serializer.save()
        if self.tags and len(self.tags) > 0:
            for tg in self.tags:
                obj = ContactTag(tag=Tag.objects.get(pk=tg),
                                 contact=Contact.objects.get(pk=instance.id))
                obj.save()
        super().perform_create(serializer)
