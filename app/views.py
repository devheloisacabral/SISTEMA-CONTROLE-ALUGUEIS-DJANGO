from django.shortcuts import render, redirect, get_object_or_404
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


def edit_property(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    form = PropertyForm(instance=property_instance)

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('list_location')

    return render(request, 'edit_property.html', {'form': form})


def delete_property(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    form = PropertyForm(instance=property_instance)

    if request.method == 'POST':
        property_instance.delete()
        return redirect('list_location')
    return render(request, 'delete_property.html', {'property': property_instance})



def register_location_form(request, id):
    get_property = Property.objects.get(id=id)
    form = RegisterLocationForm()
    if request.method == 'POST':
        form = RegisterLocationForm(request.POST)
        if form.is_valid():
            property_form = form.save(commit=False)
            property_form.property = get_property  # vai salvar o id da propriedade
            prop = Property.objects.get(id=id)
            prop.is_locate = True
            prop.save()
            property_form.save()
            return redirect(list_location)
    context = {'form': form, 'location': get_property}
    return render(request, 'form-location.html', context)


def report(request):
    property = Property.objects.all()
    is_located = request.GET.get('is_locate')
    if is_located:
        property = Property.objects.filter(is_locate=is_located)
    return render(request, 'report.html', {'property': property})
