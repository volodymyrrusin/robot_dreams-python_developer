from django.views.generic import ListView, DetailView, CreateView
from book.models import Book
from book.forms import BookForm


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
