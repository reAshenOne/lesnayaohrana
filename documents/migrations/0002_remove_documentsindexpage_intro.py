# Generated by Django 5.0.3 on 2024-03-24 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentsindexpage',
            name='intro',
        ),
    ]