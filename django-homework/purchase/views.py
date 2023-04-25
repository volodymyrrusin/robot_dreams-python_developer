from django.http import JsonResponse
from .models import Purchase


def my_view(request):
    purchases = list(Purchase.objects.all().values())
    return JsonResponse(purchases, safe=False)

