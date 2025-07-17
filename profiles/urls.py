from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='user_profile'),
    path('orders/', views.order_history, name='order_history'),
    path('orders/<order_number>/', views.order_detail, name='order_detail'),
]
