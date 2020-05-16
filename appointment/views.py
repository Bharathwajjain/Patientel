from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import forms

def index(request):
    return render(request, 'index.html')

def details(request):
    if request.method == 'POST': 
        form = forms.SimpleForm(request.POST)
        return render(request, 'details.html', {'form': form})
        
