# coding: utf-8

from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework import routers
from .views import AddrViewSet
from .views import UploadformViewSet

schema_view = get_schema_view(title='Addressess API',
                              url='https://192.168.132.129/api/',
                              renderer_classes=[JSONOpenAPIRenderer]
                              )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'addrs', AddrViewSet)
router.register(r'upload_form/(?P<filename>.*)$', UploadformViewSet, base_name='upload_form')


urlpatterns = [
    path('openapi', get_schema_view(
        title="Addresses",
        description="Addresses API", 
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
