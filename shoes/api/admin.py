from django.contrib import admin
from .models import Color, ShoeSize, Brand, Sex, Season, Shoes

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ShoeSize)
class ShoeSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'shoe_size', 'brand', 'is_published')
    list_filter = ('color', 'shoe_size', 'brand', 'is_published')
    search_fields = ('name', 'description')
    list_editable = ('is_published',)
