from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('<int:posts_id>/', views.detail_posts, name='detail'),
    path('', views.list_posts, name='index'),
    path('search/', views.search_posts, name='search'),
    path('create/', views.create_posts, name='create'),
    path('update/<int:post_id>/', views.update_posts, name='update'),
    path('delete/<int:post_id>/', views.delete_posts, name='delete'),
    path('categorias/', views.list_categorias, name='categorias'),
    path('categoria/<str:categoria>/', views.posts_by_category, name='categoria_posts'),
]