# Generated by Django 3.1.2 on 2020-10-06 16:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_project_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]