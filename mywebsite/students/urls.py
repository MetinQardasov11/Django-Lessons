from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
    path('', index, name='index'),
]