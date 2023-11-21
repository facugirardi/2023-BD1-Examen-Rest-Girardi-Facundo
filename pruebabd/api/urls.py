from django.urls import path
from .views import *

urlpatterns = [
    path('api/punto1', punto1, name='punto1'),
]
