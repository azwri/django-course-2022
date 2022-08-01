from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .serializers import FlowerSerializer
from .models import Flower

def index(request: Request):
    context = {
        'flowers': Flower.objects.all(),
    }
    return render(request=request,template_name='myapp/index.html', context=context)


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