from urllib.request import Request
from django.shortcuts import render


def index(request: Request):
    context = {}
    return render(request=request,template_name='myapp/index.html', context=context)