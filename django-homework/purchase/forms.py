from django import forms
from purchase.models import Purchase
from user.models import User
from book.models import Book


class PurchaseForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'style': 'width 80px', 'class': 'form-control'}))

    class Meta:
        model = Purchase
        fields = ('user', 'book', 'date')

