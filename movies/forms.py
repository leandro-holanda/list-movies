from django import forms
from .models import Category, Movie, AudioMovie


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'category', 'cartaz']
        widgets = {
            'cartaz': forms.FileInput(attrs={'accept': 'image/*'})
        }


class AudioMovieForm(forms.ModelForm):
    
    class Meta:
        model = AudioMovie
        fields = ['movie', 'name_audio', 'audio']
        widgets = {
            'audio': forms.FileInput(attrs={'accept': 'audio/*'})
        }