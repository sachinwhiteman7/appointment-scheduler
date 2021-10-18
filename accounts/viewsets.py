from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from accounts.models import User
from accounts.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    """ViewSet for creating a User and listing users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
