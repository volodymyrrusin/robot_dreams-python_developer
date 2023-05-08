from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from purchase.models import Purchase
from purchase.forms import PurchaseForm
from purchase.serializers import PurchaseSerializer


# class PurchaseListView(ListView):
#     model = Purchase
#
#
# class PurchaseDetailView(DetailView):
#     model = Purchase
#
#
# class PurchaseCreateView(CreateView):
#     model = Purchase
#     form_class = PurchaseForm


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    search_fields = ['user__first_name', 'book__title']
    ordering_fields = ['id', 'date']
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
