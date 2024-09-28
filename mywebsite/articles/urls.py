from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('', article_view, name='article'),
    path('science/', science_view, name='science'),
]