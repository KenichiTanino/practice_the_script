# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Addr
from .serializer import AddrSerializer


class AddrViewSet(viewsets.ModelViewSet):
    queryset = Addr.objects.all()
    serializer_class = AddrSerializer


class UploadformViewSet(viewsets.ViewSet):

    def create(self, request, filename):
        print(filename)

    def destroy(self, request, filename):
        print(filename)

