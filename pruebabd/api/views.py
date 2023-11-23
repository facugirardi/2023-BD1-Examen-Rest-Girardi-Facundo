from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .services import *

# Create your views here.

@api_view(['GET'])
def punto1(request):
    categories = CategoryService.fitrarTerminaCon('s')
    serializado = CategorySerializer(categories, many=True)

    return Response(serializado.data)


# @api_view(["GET", "POST"])
# def getAllCustomers(request):
#     if request.method == "GET":         
#         customers = Customer.objects.all()
#         customersSerializers = CustomerSerializer(customers, many=True)
#         return Response(customersSerializers.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         customerNuevo = CustomerSerializer(data = request.data)

#         if customerNuevo.is_valid():
#             customerNuevo.save()
#             return Response(customerNuevo.data, status=status.HTTP_202_ACCEPTED)
#         return Response(customerNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(["GET", "PUT", "DELETE"])
# def getCustomerById(request, pk):
#     try:
#         customer = Customer.objects.get(customerid=pk)
#     except Exception:
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     if request.method == 'GET':
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':

#         request.data['customerid'] = pk


#         if 'companyname' not in request.data:
#             request.data['companyname'] = customer.companyname
        
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         # borrar el customer seleccionado y ademas borrar todas las Orders que dependan de ese customer
#         customer.delete()
#         return Response(status=status.HTTP_200_OK)
    
