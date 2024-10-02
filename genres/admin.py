from django.contrib import admin

# Register your models here.
from .models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = ('id', 'name',)