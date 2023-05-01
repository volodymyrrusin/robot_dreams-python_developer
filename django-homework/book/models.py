from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')

    def __str__(self):
        return f'{self.id}: {self.title} {self.author}'

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])
