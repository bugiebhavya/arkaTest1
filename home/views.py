from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product,Company
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request,'home.html')

def logout(request):
    return render(request,'logout.html')


class ProductList(ListView):
    model = Product

class ProductView(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = ['product_name', 'product_id','price','created_date','company','color']
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    fields = ['product_name', 'product_id','price','created_date','company','color']
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')