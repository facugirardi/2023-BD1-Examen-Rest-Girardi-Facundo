from django.urls import path
from .views import *

urlpatterns = [
    path("api/productos", punto1 , name="punto1"),
    path("api/orders", punto2 , name="punto2"),
]
