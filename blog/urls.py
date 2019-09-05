from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_blog, name='posts_blog'),
    path('post/<str:post_id>', views.post_blog, name='post_blog'),
    path('posts/', views.all_post_blog, name='all_post_blog'),
    path('contact/', views.contact_blog, name='contacts_blog'),
    path('about/', views.about_blog, name='about_blog'),
    path('accounts/', views.accounts)
]
