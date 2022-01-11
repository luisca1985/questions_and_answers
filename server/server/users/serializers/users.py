"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate

#  Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from server.users.models import User
from server.users.models import Profile


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    class Meta:
        """Meta class."""
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email')


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializers

    Handle the sign up data validation and user creation.
    """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],

    )
    # Password
    password = serializers.CharField(min_length=4, max_length=64)
    password_confirmation = serializers.CharField(min_length=4, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify password match"""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError('Passwords do not match.')
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)
        return user



class UserLoginSerializer(serializers.Serializer):
    """User login serializers

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credential."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class AccountVerificationAPIView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
