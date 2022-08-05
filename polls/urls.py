from django.urls import path

from . import views

urlpatterns = [
    path('orders', views.orders_list),
    path('order' , views.Order.as_view())
]