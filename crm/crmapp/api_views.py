from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def contacts_api(request):
    if request.method == 'GET':
        data = Contact.objects.all()
        return Response(ContactSerializer(data, many=True).data)

    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def products_api(request):
    if request.method == 'GET':
        data = Product.objects.all()
        return Response(ProductSerializer(data, many=True).data)

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET', 'POST'])
def orders_api(request):
    if request.method == 'GET':
        data = Order.objects.all()
        return Response(OrderSerializer(data, many=True).data)

    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET', 'POST'])
def order_items_api(request):
    if request.method == 'GET':
        data = OrderItem.objects.all()
        return Response(OrderItemSerializer(data, many=True).data)

    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET', 'POST'])
def organizations_api(request):
    if request.method == 'GET':
        data = Organization.objects.all()
        return Response(OrganizationSerializer(data, many=True).data)

    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
