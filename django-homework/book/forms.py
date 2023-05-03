from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 80px', 'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'style': 'width 80px', 'class': 'form-control'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 80px', 'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width 80px', 'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'price')
