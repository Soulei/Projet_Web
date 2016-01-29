from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

def index(request):
	#template_name = 'rootsapp/index.html'
    return render(request, 'rootsapp/index.html')

