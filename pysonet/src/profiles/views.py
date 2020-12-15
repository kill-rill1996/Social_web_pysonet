from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions

from .serializers import GetUserNetSerializer
from .models import UserNet


class GetUserNetView(RetrieveAPIView):
    """Information about User"""
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer


class UpdateUserNetView(UpdateAPIView):
    """Update user info"""
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
