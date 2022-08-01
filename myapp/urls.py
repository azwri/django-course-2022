from django.urls import path
from .views import index, add_flower_api


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('add/',add_flower_api, name='add_flower_api'),
]
