from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:product_id>/', views.like_product, name='like_product'),
    path('interact/<int:product_id>/', views.submit_rating_comment, name='submit_rating_comment'),
]
