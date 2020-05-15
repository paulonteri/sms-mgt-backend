from rest_framework import routers

from .api import ContactAPI, TagAPI, ContactTagAPI

router = routers.DefaultRouter()

router.register("contact", ContactAPI, "Contact")
router.register("tag", TagAPI, "Tag")
router.register("contacttags", ContactTagAPI, "Contact Tags")

urlpatterns = router.urls
