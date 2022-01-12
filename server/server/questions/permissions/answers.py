from rest_framework import permissions

class AnswerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list','list_for_question']:
            return True
        if view.action in ['create']:
            return request.user.is_authenticated