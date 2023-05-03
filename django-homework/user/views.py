from django.views.generic import ListView, DetailView, CreateView
from user.models import User
from user.forms import UserForm


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
