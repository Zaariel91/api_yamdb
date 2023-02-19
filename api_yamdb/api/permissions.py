from rest_framework import permissions


class isAuthor_Admin_Moderator_or_ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == 'admin'
                or request.user.role == 'moderator'
                or obj.author == request.user)


class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and request.user.is_admin)
        )


# class IsAuthorOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_anonymous:
#             return request.method in permissions.SAFE_METHODS
#         return True

#     def has_object_permission(self, request, view, obj):
#         return (
#             request.method in permissions.SAFE_METHODS
#             or request.user.is_admin
#             or request.user.is_moderator
#             or request.user == obj.author
#         )


class IsGuest(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_anonymous


class AdminOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return (request.user.is_admin or request.user.is_staff)

    # def has_object_permission(self, request, view, obj):
    #     return (request.user.is_admin or request.user.is_staff)
    pass


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser
        )


# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             return request.user.is_admin
