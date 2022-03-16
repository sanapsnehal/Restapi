"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import debug_toolbar
from django.conf import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get',get_quotes),
    path('api/v1/post',post_quotes),
    path('api/v1/put',put_quotes),
    path('api/v1/delete',delete_quotes),
    # path('api/v1/category/',CategoriesList.as_view()),
    # path('api/v1/product/',ProductListView.as_view()),
    # path('api/v1/requestlog/',RequestLogListView.as_view()),
    # path('api/v1/faq',RequestLogListView.as_view()),
    path('swagger',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    # path('__debug__/', include(debug_toolbar.urls)),
    # path('api/token/',TokenObtainPairView.as_view()),
    # path('api/token/refresh/',TokenRefreshView.as_view()),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
