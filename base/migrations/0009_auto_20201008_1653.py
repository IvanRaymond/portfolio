# Generated by Django 3.1.2 on 2020-10-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20201007_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='project',
            name='projectResume',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
