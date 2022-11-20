from django.urls import path
from .views import (
    order_list_view,
    order_create_view,
    order_update_view,
    order_accepted_list_view
)

app_name = 'orders'
urlpatterns = [
    path('', order_list_view, name='order-list'),
    path('accepted', order_accepted_list_view, name='order-accepted-list'),
    path('create/', order_create_view, name='order-create'),
    path('<int:id>/update/', order_update_view, name='order-update'),
]
