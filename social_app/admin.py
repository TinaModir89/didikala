from django.contrib import admin
from .models import point , is_Useful , comment , image 

@admin.register(point)
class pointAdmin(admin.ModelAdmin):
    pass


@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    pass


@admin.register(is_Useful)
class is_usefulAdmin(admin.ModelAdmin):
    pass


@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    pass

