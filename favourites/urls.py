from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('add/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'),
]