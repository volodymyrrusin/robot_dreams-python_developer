from django.views.generic import ListView, DetailView, CreateView
from purchase.models import Purchase
from purchase.forms import PurchaseForm


class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
