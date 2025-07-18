from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:product_id>/', views.like_product, name='like_product'),
    path('rate/<int:product_id>/', views.submit_rating, name='submit_rating'),
    path('comment/<int:product_id>/', views.submit_comment, name='submit_comment'),
]
