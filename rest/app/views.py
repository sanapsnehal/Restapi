from itertools import product
from turtle import title
from unicodedata import category
from urllib import response
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# from rest_framework.parser import JsonParser
from django.conf.urls import url
# from rest_framwework_swagger.views import get_swagger_view
from serializers import QuotesSerializers,CategoriesSerializers,ProductsSerializers,RequestLogSerializers,FaqSerializers
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import *
from rest_framework.mixins import ListModelMixin
from django.contrib.auth.models import Group
import math,random


# Create your views here.
# @api_view(['GET'])
def get_quotes(request):
    pagination = PageNumberPagination()
    pagination.page_size = 5
    quotes = Quote.objects.all()
    result_page = pagination.paginate_queryset(quotes, request)
    serializer = QuotesSerializers(result_page,many=True)
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'email']
    # name='quotes'
    # filter_field=('title')
    # return Quote.objects.filter(Quote=title)
    return pagination.get_paginated_response(serializer.data)
    # return Response(serializer.data)

@api_view(['POST'])
def post_quotes(request):
    serializer = QuotesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_quotes(request,id):
    quotes=Quote.objects.get(id=id)
    serializer=QuotesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error,status=400)

@api_view(['DELETE'])
def delete_quotes(request,id):
    quotes=Quote.objects.get(id=id)
    quotes.delete()
    return Response(status=204)

# class standardresultssetpagination(PageNumberPagination):
#     page_size=1
#     page_size_query_param='page_size'
#     max_page_size=2
 # pagination=standardresultssetpagination
    # permission_classes([IsAuthenticated])
# class CategoriesList(APIView):
#     def get(self,request):
#         categories=Category.objects.all()
#         serializer=CategoriesSerializers(categories,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=CategoriesSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class ProductListView(APIView):
#     def get(self,request):
#         product=Product.objects.all()
#         serializer=ProductsSerializers(product,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=ProductsSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class RequestLogListView(APIView):
#     def get(self,request):
#         requestlog=RequestLog.objects.all()
#         serializer=RequestLogSerializers(RequestLog,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=RequestLogSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class FaqListView(APIView):
#     def get(self,request):
#         faq=Faq.objects.all()
#         serializer=FaqSerializers(Faq,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=FaqSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     # def put(self,request,pk):
#     #     serializer = CategoriesSerializers(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=400)
    
# # class ProductListView(GenericAPIView,
# #                       mixins.ListModelMixin,
# #                       mixins.CreateModelMixin,
# #                       mixins.UpdateModelMixin):
# #     serializer=ProductsSerializers
# #     queryset=Product.objects.all()
# #     def get(self, request):
# #         return self.list(request)
    
# #     def post(self,request):
# #         return self.create(request)
    
# #     def put(self,request,id=None):
# #         return self.update(request,id)

# #     def delete(self,request,id=None):
# #         return self.delete(request,id)


# def generateOTP():
#     digits = "0123456789"
#     OTP = ""
#     for i in range(4):
#         OTP += digits[math.floor(random.random()*10)]
#         return OTP




