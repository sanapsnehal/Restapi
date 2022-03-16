from rest_framework import serializers
from .models import Category, Faq, Quote, Product, RequestLog

class QuotesSerializers(serializers.ModelSerializer):
    class Meta:
        model= Quote
        fields= '__all__'

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class RequestLogSerializers(serializers.ModelSerializer):
    class Meta:
        model=RequestLog
        fields='__all__'

class FaqSerializers(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields='__all__'