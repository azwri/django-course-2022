from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from .serializers import FlowerSerializer
from .models import Flower, Category


def index(request: Request):
    context = {
        'flowers': Flower.objects.all(),
    }
    return render(request=request,template_name='myapp/index.html', context=context)


def detail(request: Request, slug: str):
    flower = get_object_or_404(Flower, slug=slug)
    contentx = {'flower': flower}
    return render(request=request, template_name='myapp/detail.html', context=contentx)

def category(request: Request):
    category =  Category.objects.all()
    context = {'category': category}
    return render(request=request, template_name='myapp/category.html', context=context)
    





# api

@api_view(['POST'])
def add_flower_api(request: Request):
    flower = FlowerSerializer(data=request.data)

    if flower.is_valid():
        flower.save()
    else:
        return Response({'msg': 'Could not create flower', 'errors': flower.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({
        'msg': 'Flower added successfully'
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_flower_api(request: Request, pk: int):
    flower = get_object_or_404(Flower, pk=pk)
    return Response(FlowerSerializer(flower).data)

