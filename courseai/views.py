from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request, 'index.html')
    # return render(request, 'mask.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

    
def overview(request):
    return render(request, 'overview.html')

def blog(request):
    return render(request, 'blog.html')

    
def post1(request):
    return render(request, 'post.html')
