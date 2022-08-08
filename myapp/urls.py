from django.urls import path
from .views import index, detail,category, category_detail, tag_detail
from .views import add_flower_api, get_flower_api


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('flower/<slug:slug>/', detail, name='detail'),
    path('flower/category/all/', category, name='category'),
    path('flower/category/<slug:slug>/', category_detail, name='category_detail'),
    path('flower/tag/<slug:slug>/', tag_detail, name='tag_detail'),


    # api
    path('api/get/<int:pk>/', get_flower_api, name='get_flower_api'),
    path('api/add/',add_flower_api, name='add_flower_api'),
]
