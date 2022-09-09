from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import Group
from .serializers import GroupCreateSerializer, GroupSerializer
from .utils.mixins import SerializerByMethodMixin


class GroupView(SerializerByMethodMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Group.objects.all()
    serializer_map = {
        "GET": GroupSerializer,
        "POST": GroupCreateSerializer,
    }

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


class GroupDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
