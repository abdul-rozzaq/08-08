from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Forum

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class ForumSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Forum
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data["username"], password=validated_data["password"])
