from django.contrib import admin

# Register your models here.

from .models import Quote
from .models import Category
from .models import Product
from .models import RequestLog
from .models import Faq

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']

class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['request_method']

class FaqAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(Quote)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(RequestLog)
admin.site.register(Faq)