# coding: utf-8

from rest_framework import serializers

from .models import Addr


class AddrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addr
        fields = (
            'id',
            'name',
            'birthday',
            'gender',
            'address',
            'jobs',
            'note',
            'created_at',
            'updated_at')


class UploadformSerializer(serializers.Serializer):
    result = serializers.CharField()
    filename = serializers.CharField()
