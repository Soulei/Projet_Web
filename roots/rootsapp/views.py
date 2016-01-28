from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

def index():
    template_name = 'templates/rootsapp/index.html'
    return render(request, template_name)

