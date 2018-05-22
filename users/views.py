from rest_framework import generics
from rest_framework.pagination import CursorPagination

from users.models import User
from users.serializers import UserSerializer


class CursorSetPagination(CursorPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    ordering = 'date_joined'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CursorSetPagination


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def get_queryset(self):
    #     return User.objects.all().filter(username=self.request.user)
