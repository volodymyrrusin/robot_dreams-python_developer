from celery import shared_task
from purchase.models import Purchase


@shared_task
def purchases_task(user_id):
    purchases = Purchase.objects.filter(user=user_id)
    print(f'Number of purchases is: {purchases.count()}')
