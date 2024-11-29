from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_reviews, name='product_reviews'),
    path('<int:product_id>/add/', views.add_review, name='add_review'),
    path('<int:review_id>/edit/', views.edit_review, name='edit_review'),
     path('<int:review_id>/delete/', views.delete_review, name='delete_review'), 
]