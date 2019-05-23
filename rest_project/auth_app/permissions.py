from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyPOSTForNoAuthUser(BasePermission):
    message = 'You must be owner of this object'

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            if request.method in ['POST']:
                return True
            return False

    # def has_object_permission(self, request, view, obj):
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return obj == request.user or request.user.is_superuser


class WithOutPOSTForAuthUser(BasePermission):
    message = 'hello'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in ['GET', 'PUT', 'DELETE'] or request.user.is_superuser:
                return True
            return False