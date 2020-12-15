from rest_framework.generics import RetrieveAPIView

from .serializers import GetUserNetSerializer
from .models import UserNet


class GetUserNetView(RetrieveAPIView):
    """Information about User"""
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer
