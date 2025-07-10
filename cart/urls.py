from django.urls import path
from . import views


urlpatterns = {
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.view_cart, name='view_cart'),
}
