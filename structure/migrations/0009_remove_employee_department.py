# Generated by Django 5.0.3 on 2024-03-24 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0008_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
    ]