from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'product', 'rating', 'created_at')
    search_fields = ('title', 'content', 'user__username', 'product__name')
    list_filter = ('rating', 'created_at')
