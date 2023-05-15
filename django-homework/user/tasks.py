from celery import shared_task
from user.models import User


@shared_task
def my_task():
    print('This is some text')


@shared_task
def scheduled_task():
    users = User.objects.all()
    print(f'Number of users: {users.count()}')
