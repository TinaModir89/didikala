from django.contrib import admin
from .models import profile , address

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    pass

@admin.register(address)
class addressAdmin(admin.ModelAdmin):
    pass
