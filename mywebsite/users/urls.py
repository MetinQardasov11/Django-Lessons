from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile')
]