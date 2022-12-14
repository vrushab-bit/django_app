from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OwnerSerializer, ShopSerializer, ProductSerializer
from .models import Owner, Shop, Product


class OwnerView(APIView):
    def post(self, request):
        data = request.data
        serializer = OwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)


class ShopView(APIView):
    def post(self, request):
        data = request.data
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


"""
Todo

/owners -> post  -> add owner -> can be done only by admin(superuser)
/owners -> get  -> get List of owners -> can be done only by admin(superuser)






/shops -> post -> Add a shop -> can be done by owner
/shops -> get -> get list of shops owned by the owner -> can be done by owner
/products -> post -> add a product 
/products -> get -> get list of products by shop  






"""
