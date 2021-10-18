from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from timeslots.models import TimeSlot
from timeslots.serializers import TimeSlotSerializer


class TimeSlotViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    """ViewSet for creating a User."""

    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = (AllowAny, )
