from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status

from .models import User
from .permissions import IsAdmin, IsOwnerOrAdmin
from .serializers import LoginSerializer, UserSerializer


class UserView(generics.CreateAPIView, generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin, IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin, IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserLogin(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid username or password"},
            status=status.HTTP_400_BAD_REQUEST,
        )
