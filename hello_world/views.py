from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
def index(request):
    # Logic 
    return render(request, 'hello_world/index.html')
