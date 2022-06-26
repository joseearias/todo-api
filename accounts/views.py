from rest_framework import generics

from django.contrib.auth import get_user_model

from .serializers import UserSerializer


class ListUsers(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class DetailUsers(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer