from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from user.models import User
from user.forms import UserForm
from user.serializers import UserSerializer


# class UserListView(ListView):
#     model = User
#
#
# class UserDetailView(DetailView):
#     model = User
#
#
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm

class CustomPaginator(PageNumberPagination):
    page_size = 10


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPaginator
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['id', 'age']
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

