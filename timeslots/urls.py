from django.conf.urls import url, include
from rest_framework import routers

from timeslots.views import CommonTimeSlotsApiView
from timeslots.viewsets import TimeSlotViewSet


router = routers.DefaultRouter()
router.register(r'', TimeSlotViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('common-slots', CommonTimeSlotsApiView.as_view())
]
