"""table_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

from django.urls import include
from tableapp.urls import router as tableapp_router

from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer

schema_view = get_schema_view(title='Addressess API',
                              url='https://192.168.132.129/api/',
                              renderer_classes=[JSONOpenAPIRenderer]
                              )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(tableapp_router.urls)),
    path('openapi/', get_schema_view(title="Addresses",
                                    description="Addresses API",
                                    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html',
                                            extra_context={'schema_url':'openapi-schema'}
                                            ), name='swagger-ui'),
]
