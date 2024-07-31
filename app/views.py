from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_location(request):
    properties = Property.objects.filter(is_locate=False)
    context = {'properties': properties}
    return render(request, 'list_location.html', context)

def form_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_location)
    return render(request, 'form_client.html', {'form': form})