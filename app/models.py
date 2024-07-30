from django.db import models
from datetime import datetime


class TypeProperty(models.TextChoices):
    APARTAMENT = 'APARTAMENT', 'APARTAMENT'
    HOUSE = 'HOUSE', 'HOUSE'
    KITNET = 'KITNET', 'KITNET'


class Property(models.Model):
    address = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    is_locate = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type_item = models.CharField(max_length=50, choices=TypeProperty.choices)

    def __str__(self):
        return "{}-{}".format(self.code, self.type_item)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        ordering = ['-id']


class Client(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return "{}-{}".format(self.name, self.email)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['-id']


class RegisterLocation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_location')
    dt_end = models.DateTimeField('End')
    dt_start = models.DateTimeField('Start')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "{}-{}".format(self.client, self.property)

    class Meta:
        verbose_name = 'Register Location'
        verbose_name_plural = 'Register Locations'
        ordering = ['-id']


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_image')
    image = models.ImageField('Images', upload_to='images/')

    def __str__(self):
        return self.property.code
