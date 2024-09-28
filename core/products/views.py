from typing import Any
from django.db.models.query import QuerySet
from django.db.models import F
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product
from django.views.generic import View, TemplateView, ListView, DetailView

# Create your views here.

# def product_list(request):
#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#     else:
#         product_name = 'No product name provided'
    
#     print(product_name)
#     print(request.resolver_match.url_name)
    
#     return render(request, 'products.html')


# class ProdutView(View):
#     http_method_names = ['get', 'post']
    
#     def get(self, request):
#         print(request.method)
#         return render(request, template_name='products.html')
    
#     def post(self, request):
#         print(request.method)
#         return render(request, template_name='products.html')
    
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    

# class AboutView(TemplateView):
#     template_name = 'about.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['dynamic_data'] = 'My name is John'
#         return context


class ProductListView(ListView):
    template_name = 'product_list.html'
    # queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 2
    page_kwarg = 'page'
    
    def get_queryset(self) -> QuerySet[Any]:
        stock = self.request.GET.get('stock')
        if stock:
            stock = int(stock)
            return Product.objects.filter(stock=stock)
        return Product.objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['pl'] = 'Python'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        return super().get_queryset().annotate(
            total_price = F('price') - F('discount')
        )