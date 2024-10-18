from django.contrib import admin
from .models import Product, Category, ProductSize

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

# productsize admin
# display productsize fields in admin
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'size',
        'price',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
