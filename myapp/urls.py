from django.urls import path
from .views import index, detail
from .views import add_flower_api, get_flower_api


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('flower/<slug:slug>/', detail, name='detail'),


    # api
    path('api/get/<int:pk>/', get_flower_api, name='get_flower_api'),
    path('api/add/',add_flower_api, name='add_flower_api'),
]
