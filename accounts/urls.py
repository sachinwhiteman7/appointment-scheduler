from django.conf.urls import url, include
from rest_framework import routers

from accounts.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
