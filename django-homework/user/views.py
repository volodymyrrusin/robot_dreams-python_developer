from django.http import JsonResponse
from .models import User


def my_view(request):
    users = list(User.objects.all().values())
    return JsonResponse(users, safe=False)
