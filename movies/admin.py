from django.contrib import admin

# Register your models here.
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('id', 'title', 'release_date')