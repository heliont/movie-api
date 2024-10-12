from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class Actor(admin.ModelAdmin):
    model = Actor
    list_display = ('id', 'name', 'birthday', 'nationality')
