# Generated by Django 5.0.3 on 2024-03-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_remove_substructure_structure_page_subdivision_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdivision',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
