from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from .serializers import UsersSerializer
from rest_framework.response import Response

from .permissions import (
    IsOwnerOrReadOnly,
)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = get_user_model().objects.all().order_by('id')
    serializer_class = UsersSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)