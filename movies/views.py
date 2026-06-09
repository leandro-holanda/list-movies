from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Category, Movie, AudioMovie
from .forms import MovieForm, AudioMovieForm, CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    ordering = ['name']

    def get_queryset(self):
        return super().get_queryset().prefetch_related('movie_set')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['audios'] = AudioMovie.objects.filter(movie__category=self.object).select_related('movie')
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        movie_name = self.request.GET.get('name')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if movie_name:
            queryset = queryset.filter(name__icontains=movie_name)
        return queryset.select_related('category').prefetch_related('audiomovie_set')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['audios'] = self.object.audiomovie_set.all()
        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


class AudioMovieListView(ListView):
    model = AudioMovie
    template_name = 'audio_list.html'
    context_object_name = 'audios'
    ordering = ['-data_upload']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        movie_id = self.request.GET.get('movie')
        category_id = self.request.GET.get('category')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        if category_id:
            queryset = queryset.filter(movie__category_id=category_id)
        return queryset.select_related('movie__category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', '')
        return context


class AudioMovieDetailView(DetailView):
    model = AudioMovie
    template_name = 'audio_detail.html'
    context_object_name = 'audio'


class AudioMovieCreateView(LoginRequiredMixin, CreateView):
    model = AudioMovie
    form_class = AudioMovieForm
    template_name = 'audio_form.html'
    success_url = reverse_lazy('audio_list')

    def get_initial(self):
        initial = super().get_initial()
        movie_id = self.request.GET.get('movie')
        if movie_id:
            initial['movie'] = movie_id
        return initial


class AudioMovieUpdateView(LoginRequiredMixin, UpdateView):
    model = AudioMovie
    form_class = AudioMovieForm
    template_name = 'audio_form.html'
    success_url = reverse_lazy('audio_list')


class AudioMovieDeleteView(LoginRequiredMixin, DeleteView):
    model = AudioMovie
    template_name = 'audio_confirm_delete.html'
    success_url = reverse_lazy('audio_list')