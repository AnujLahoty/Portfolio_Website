# Generated by Django 4.0.3 on 2022-04-06 07:45

from django.db import migrations
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skills',
            field=portfolio.models.ListField(default=[], token=','),
        ),
    ]
