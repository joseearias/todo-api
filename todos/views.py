from rest_framework import generics, permissions

from .models import Todo
from .permissions import IsAuthor
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all().filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthor,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
