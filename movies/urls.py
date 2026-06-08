from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    # Movie URLs
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('movies/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    
    # Audio URLs
    path('audios/', views.AudioMovieListView.as_view(), name='audio_list'),
    path('audios/<int:pk>/', views.AudioMovieDetailView.as_view(), name='audio_detail'),
    path('audios/create/', views.AudioMovieCreateView.as_view(), name='audio_create'),
    path('audios/<int:pk>/update/', views.AudioMovieUpdateView.as_view(), name='audio_update'),
    path('audios/<int:pk>/delete/', views.AudioMovieDeleteView.as_view(), name='audio_delete'),
]