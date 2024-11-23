from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if request.method == "POST":
            return request.user.is_authenticated

        if request.method in ["PUT", "PATCH", "DELETE"]:
            return view.get_object().creator == request.user

        return False

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == "POST":
            return True

        if request.method in ["PUT", "PATCH", "DELETE"]:
            return obj.creator == request.user

        return False
