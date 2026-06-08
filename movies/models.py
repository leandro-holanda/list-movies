from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name    


class AudioMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    name_audio = models.CharField(max_length=255)
    audio = models.FileField(upload_to='audios/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} - {self.name_audio}'