# Generated by Django 4.0.6 on 2022-08-09 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter_images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]