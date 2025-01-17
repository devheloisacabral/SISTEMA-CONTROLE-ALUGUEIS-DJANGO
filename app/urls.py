"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.list_location, name='list_locationn'),
    path('location', app.views.list_location, name='list_location'),
    path('form-client', app.views.form_client, name='client-create'),
    path('form-property', app.views.form_property, name='property-create'),
    path('property/<int:pk>/edit/', app.views.edit_property, name='edit_property'),
    path('property/<int:pk>/delete/', app.views.delete_property, name='delete_property'),
    path('form-location/<int:id>/', app.views.register_location_form, name='location-create'),
    path('reports/', app.views.report, name='reports'),
    path('reports/<int:pk>/edit', app.views.edit_property_status, name='edit_property_status')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
