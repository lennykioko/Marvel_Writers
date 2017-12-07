"""Creates the views for the home and about page"""
from django.shortcuts import render

# Create your views here.
def home(request):
    """Renders the home page"""
    context = {}
    template = 'index.html'
    return render(request, template, context)

def about(request):
    """Renders the about page"""
    context = {}
    template = 'about.html'
    return render(request, template, context)
