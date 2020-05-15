from rest_framework import routers

from .api import ContactAPI

router = routers.DefaultRouter()

router.register("contact", ContactAPI, "Contact")

urlpatterns = router.urls
