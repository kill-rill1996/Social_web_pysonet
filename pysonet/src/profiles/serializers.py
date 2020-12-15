from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Show info about User"""
    class Meta:
        model = UserNet
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """Show public info about User"""
    class Meta:
        model = UserNet
        exclude = (
            'email',
            'phone',
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )
