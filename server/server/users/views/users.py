# Django Rest Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from server.users.models import User

# Serializers
from server.users.serializers import (
    UserModelSerializer,
    UserSignUpSerializer,
    UserLoginSerializer, 
    AccountVerificationAPIView)


class UserViewSet(viewsets.ModelViewSet):
    """User view set.

    Handle sign up, login and account verification
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account Verification."""
        serializer = AccountVerificationAPIView(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulations, now go to ask and answer.'}
        return Response(data, status=status.HTTP_200_OK)
