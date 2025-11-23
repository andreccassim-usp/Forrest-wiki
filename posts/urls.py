from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('<int:posts_id>/', views.Posts, name='post'),
    path('', views.list_posts, name='index'),
    path('search/', views.search_posts, name='search'),
    path('create/', views.create_posts, name='create'),
]