from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/delete/<int:id>', views.delete_cart, name='delete_cart'),
]
