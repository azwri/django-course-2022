from django.contrib import admin
from .models import Flower


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    
