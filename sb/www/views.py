from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts':posts})