from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def punto1(request):
    customers = Category.objects.all()
    serializado = CategorySerializer(customers, many=True)

    return Response(serializado.data)