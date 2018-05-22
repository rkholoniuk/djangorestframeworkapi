from rest_framework import generics
from rest_framework.pagination import CursorPagination
from todos.models import Todo
from todos.serializers import TodoSerializer


class CursorSetPagination(CursorPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    ordering = 'created'


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CursorSetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    # def get_queryset(self):
    #     return Todo.objects.all().filter(user=self.request.user)
