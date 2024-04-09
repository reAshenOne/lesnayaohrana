# Generated by Django 5.0.3 on 2024-03-24 13:10

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0006_structurepage_departments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structurepage',
            name='departments',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='structure.department'),
        ),
    ]
