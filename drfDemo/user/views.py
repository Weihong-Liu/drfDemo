# django库
from django.contrib.auth import get_user_model
# rest_framework库
from rest_framework import viewsets
from rest_framework import mixins
# app
from .serializers import UserRegSerializer

User = get_user_model()


class UserRegViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    queryset = User.objects.all()