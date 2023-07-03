# rest_framework库
from rest_framework import serializers
# django库
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "password")