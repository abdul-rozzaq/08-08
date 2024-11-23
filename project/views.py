from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Comment, Forum
from .permissions import IsCreator
from .serializers import CommentSerializer, ForumSerializer, RegisterSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = [IsCreator]

    def perform_create(self, serializer):
        return serializer.save(creator_id=self.request.user.id)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCreator]

    def perform_create(self, serializer):
        return serializer.save(creator_id=self.request.user.id)


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Ro'yhatdan o'tish",
        operation_id="register",
        operation_description="Ro'yxatdan o'tish uchun API",
        request_body=RegisterSerializer,
        tags=["auth"],
    )
    def post(self, request: Request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({"message": "User created successfully", "access_token": access_token, "refresh_token": str(refresh)})
