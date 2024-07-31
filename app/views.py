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


def form_property(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_save = form.save()
            files = request.FILES.getlist('property_save')
            if files:
                for file in files:
                    PropertyImage.objects.create(property_save=property_save, imagem=file)
            return redirect(list_location)
    return render(request, 'form_property.html', {'form': form})
