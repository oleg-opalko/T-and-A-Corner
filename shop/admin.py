from django.contrib import admin

from .models import Brand, Category, Perfume


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'product_type', 'is_featured', 'is_available')
    list_filter = ('is_available', 'is_featured', 'brand', 'category')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'brand__name', 'category__name')
