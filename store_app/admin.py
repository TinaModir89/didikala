from django.contrib import admin
from .models import brand , digital_product , clothes_product , Color , banner , image , category ,SpecialFeature , Description , Specifications , SpecificationDetail
from django.contrib.contenttypes.admin import GenericStackedInline

class image_inlines(GenericStackedInline):
    model = image
    extra = 1


@admin.register(brand)
class brandAdmin(admin.ModelAdmin):
    pass


@admin.register(digital_product)
class digital_productAdmin(admin.ModelAdmin):
    inlines = [image_inlines]


@admin.register(clothes_product)
class clothes_productAdmin(admin.ModelAdmin):
    inlines = [image_inlines]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(banner)
class bannerAdmin(admin.ModelAdmin):
    inlines = [image_inlines]


@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    pass

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecialFeature)
class SpecialFeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Specifications)
class SpecificationsAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecificationDetail)
class SpecificationDetailAdmin(admin.ModelAdmin):
    pass