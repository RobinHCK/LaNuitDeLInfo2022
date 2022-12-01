# Import
# - Django
from django.shortcuts import render
from django.views import generic


def index(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    
    
def equipe(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'equipe.html', context=context)
    
def generation_logo(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'generation_logo.html', context=context)
