from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('add/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'), # add to favourites
    path('remove/<int:product_id>/', views.remove_from_favourites, name='remove_from_favourites'),
]


