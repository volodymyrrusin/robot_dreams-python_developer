from django.db import models


class Purchase(models.Model):
    user = models.ForeignKey('user.User', related_name='purchases', on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', related_name='purchases', on_delete=models.CASCADE)
    date = models.DateField(null=False)

    class Meta:
        db_table = 'purchase'
        ordering = ['-date']
