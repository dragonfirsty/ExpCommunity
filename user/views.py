from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.
class UserView(generics.CreateAPIView,generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = UserSerializer
     queryset = User.objects.all()  