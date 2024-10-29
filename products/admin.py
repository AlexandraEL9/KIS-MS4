from django.contrib import admin
from .models import Product, Category

# Register your models here.

# product admin
# displays product fields
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )
    # order list of products by sku
    ordering = ('sku',)

# category admin
# display both names so easy to manage
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
