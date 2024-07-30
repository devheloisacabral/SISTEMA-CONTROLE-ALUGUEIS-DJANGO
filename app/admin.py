from django.contrib import admin
from . import models

# Register your models here.

class PropertyImageAdmin(admin.TabularInline):
    model = models.PropertyImage
    extra = 0


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

admin.site.register(models.Property, PropertyAdmin)