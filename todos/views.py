from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers


class ListTodo(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
