from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:product_id>/', views.like_product, name='like_product'),
    path('rate/<int:product_id>/', views.submit_rating, name='submit_rating'),
    path('comment/<int:product_id>/', views.submit_comment,
         name='submit_comment'),
    path('liked/', views.liked_products, name='liked_products'),
    path('comments/', views.user_comments, name='user_comments'),
    path('unlike/<int:product_id>/', views.remove_like, name='remove_like'),
    path('comment/edit/<int:comment_id>/', views.edit_comment,
         name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
]
