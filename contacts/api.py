from rest_framework import permissions
from rest_framework import viewsets

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
            self.tags = request.data["tags"]
        except Exception:
            pass
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # get contact
        instance = serializer.save()
        if self.tags and len(self.tags) > 0:
            tg_obj_list = []
            for tg in self.tags:
                tg_obj_list.append(ContactTag(tag=Tag.objects.get(pk=tg),
                                              contact=Contact.objects.get(pk=instance.id),
                                              user=self.request.user))
            ContactTag.objects.bulk_create(tg_obj_list)
        super().perform_create(serializer)

    def update(self, request, *args, **kwargs):
        if request.data["tags"]:
            self.tags = (request.data["tags"])

        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        #
        print("perform_update")
        instance = serializer.save()
        #
        cont_t_list = []
        if instance and self.tags:
            ContactTag.objects.filter(contact_id=instance.pk).delete()
            #
            for q in self.tags:
                cont_t_list.append(ContactTag(contact_id=instance.pk, tag_id=q, user=self.request.user))

            ContactTag.objects.bulk_create(cont_t_list)
        #
        super().perform_update(serializer)
