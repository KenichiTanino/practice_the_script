from django.contrib import admin

from .models import Addr


@admin.register(Addr)
class AddrAdmin(admin.ModelAdmin):
        pass
