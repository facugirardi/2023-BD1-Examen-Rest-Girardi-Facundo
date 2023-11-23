from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .services import *
from datetime import datetime

#GET:/api/productos?supplierid=<id proveedor>&categoryid=<idcategoría>&stockmin=<cantidad esperada de stock>)

@api_view(["GET"])
def punto1(request):

    stockmin = request.query_params['stockmin']

    try:
        supplierid = request.query_params['supplierid']
        categoryid = request.query_params['categoryid']
        try:
            productos = Product.objects.filter(supplier=supplierid, category=categoryid, discontinued = 0, units_in_stock__lt = stockmin)

        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializado = ProductSerializer(productos, many=True)
    return Response(serializado.data, status=status.HTTP_200_OK)



# api/orders?customerid=1&employeeid=8&shipperid=5&stockRequerido=10&categoryid=1&supplierid=6

@api_view(["POST"])
def punto2(request):
    customerid = request.query_params['customerid']
    employeeid = int(request.query_params['employeeid'])
    shipperid = request.query_params['shipperid']
    stockRequerido = int(request.query_params['stockRequerido']) #filtro
    categoryid = int(request.query_params['categoryid']) #filtro
    supplierid = int(request.query_params['supplierid']) #filtro

    productos = Product.objects.filter(supplier=supplierid, category=categoryid, units_in_stock__lt = stockRequerido)


    stock_futuro = sum(producto.units_in_stock + producto.units_on_order for producto in productos)
    cant_productos = stock_futuro - stockRequerido
    precio_unitario = [producto.unit_price for producto in productos]


    if cant_productos < 100:
        descuento = 0
    else:
        descuento = 0.10

    date = datetime.now()

    try:
        employee = Employee.objects.get(id=employeeid)
        shipper = Shipper.objects.get(id=shipperid)
        customer = Customer.objects.get(id=customerid)

        ship_name = customer.contact_name
        ship_address = customer.address
        ship_city = customer.city
        ship_region = customer.region
        ship_postal_code = customer.postal_code
        ship_country = customer.country

    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)


    order = Order.objects.create(order_date = date, required_date = date, shipped_date = date, freight = 0, 
                                 ship_name = ship_name, ship_address = ship_address, ship_city = ship_city,
                                 ship_region = ship_region, ship_postal_code = ship_postal_code, ship_country = ship_country,
                                 employee = employee, customer = customer, ship_via = shipper)
    
    order_id = Order.objects.get(id=order.id)
   
    try:
        product_id = Product.objects.get(supplier=supplierid)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)

    OrderDetails.objects.create(unit_price = precio_unitario, quantity = cant_productos, discount = descuento, order_id = order_id, product_id = product_id)
    
    serializado = OrderSerializer(order, many=True)
    return Response(serializado.data, status=status.HTTP_200_OK)


    