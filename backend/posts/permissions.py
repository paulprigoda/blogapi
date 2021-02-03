from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #read only for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permissions for author of post only
        return obj.author == request.user

