from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
