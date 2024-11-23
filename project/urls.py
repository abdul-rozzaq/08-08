from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, ForumViewSet, RegisterAPIView

router = DefaultRouter()

router.register("forum", ForumViewSet)
router.register("comment", CommentViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterAPIView.as_view()),
]
