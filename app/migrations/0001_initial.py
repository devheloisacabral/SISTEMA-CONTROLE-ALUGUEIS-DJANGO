# Generated by Django 5.0.7 on 2024-07-30 22:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=50)),
                ('is_locate', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type_item', models.CharField(choices=[('APARTAMENT', 'APARTAMENT'), ('HOUSE', 'HOUSE'), ('KITNET', 'KITNET')], max_length=50)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Images')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_image', to='app.property')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_end', models.DateTimeField(verbose_name='End')),
                ('dt_start', models.DateTimeField(verbose_name='Start')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_location', to='app.property')),
            ],
            options={
                'verbose_name': 'Register Location',
                'verbose_name_plural': 'Register Locations',
                'ordering': ['-id'],
            },
        ),
    ]
