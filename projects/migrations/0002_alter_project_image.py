# Generated by Django 4.1.3 on 2022-11-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FilePathField(path="/projects/img"),
        ),
    ]
