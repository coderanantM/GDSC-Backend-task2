from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Order
from .mixins import IsAuthenticatedMixin

class OrderListView(IsAuthenticatedMixin, ListView):
    model = Order

    def get_queryset(self):
        if self.request.GET.get('search'):
            return Order.objects.filter(order_name__icontains=self.request.GET.get('search'))
        return Order.objects.filter(user = self.request.user)

class OrderCreateView(IsAuthenticatedMixin, CreateView):
    model = Order
    fields = ['order_name', 'quantity']
    success_url = reverse_lazy('order_list')

    def form_valid( self, form):

        instance = form.save( commit = False)
        instance.user = self.request.user
        instance.save()

        return HttpResponseRedirect( self.success_url)

class OrderUpdateView(IsAuthenticatedMixin, UpdateView):
    model = Order
    fields = ['order_name', 'quantity']
    success_url = reverse_lazy('order_list')

class OrderDeleteView(IsAuthenticatedMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
