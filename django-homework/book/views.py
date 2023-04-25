from django.http import JsonResponse
from .models import Book


def my_view(request):
    books = list(Book.objects.all().values())
    return JsonResponse(books, safe=False)