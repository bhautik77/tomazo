from django.urls import path
from .views import (
    order_list_view,
    order_create_view,
    order_accepted_list_view,
    order_detail_view,
    item_view
)

app_name = 'orders'
urlpatterns = [
    path('', order_list_view, name='order-list'),
    path('<int:id>/detail/', order_detail_view, name='order-detail'),
    path('accepted/', order_accepted_list_view, name='order-accepted-list'),
    path('create/', order_create_view, name='order-create'),
    path('items/', item_view, name='item-view'),
]
