from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    # path('products/', product_list, name='products')
    # path('products/', ProdutView.as_view(), name='products'),
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('about/', AboutView.as_view(), name='about'),
]