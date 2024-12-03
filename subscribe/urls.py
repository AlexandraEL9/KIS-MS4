from django.urls import path
from . import views
from .views import subscribe

urlpatterns = [
    path('', subscribe, name='subscribe'),
]