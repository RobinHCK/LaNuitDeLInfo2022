# Import
# - Django
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

from .forms import ImageGeneratorForm
from .ai.dall_e import create_DALL_E_image

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

def data_story(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'data_story.html', context=context)
    
def generation_logo(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'generation_logo.html', context=context)
 

def generation_meme(request):
    # if this is a POST request we need to process the form data
    context={}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImageGeneratorForm(request.POST)
        context['form'] = form
        
        # check whether it's valid:
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            text_overlay = form.cleaned_data['text_overlay']
            # Generate image
            image_url = create_DALL_E_image(sentence, text_overlay, 256)
            # Add image to context
            context['image_url'] = image_url


    context['form'] = ImageGeneratorForm()
    return render(request, 'generation_meme.html', context=context)

def predictions_ia(request):
    context = {}
    return render(request, 'prediction_IA.html', context=context)
