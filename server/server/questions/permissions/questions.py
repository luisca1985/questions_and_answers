from rest_framework import permissions

class QuestionPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list','retrieve']:
             return True
        if view.action in ['create']:
            return request.user.is_authenticated