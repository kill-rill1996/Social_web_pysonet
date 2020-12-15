from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer
from .models import UserNet


# class UpdateUserNetView(UpdateAPIView):
#     """Update user info"""
#     serializer_class = GetUserNetSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return UserNet.objects.filter(id=self.request.user.id)


class UserNetPublicView(ModelViewSet):
    """Information about public profile"""
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class GetUserNetView(ModelViewSet):
    """Information about User"""
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
