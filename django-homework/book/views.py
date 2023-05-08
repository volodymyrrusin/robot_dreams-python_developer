from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from book.models import Book
from book.forms import BookForm
from book.serializers import BookSerializer


# class BookListView(ListView):
#     model = Book
#
#
# class BookDetailView(DetailView):
#     model = Book
#
#
# class BookCreateView(CreateView):
#     model = Book
#     form_class = BookForm


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title', 'author']
    ordering_fields = ['id', 'year', 'price']
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
