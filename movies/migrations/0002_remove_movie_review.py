# Generated by Django 4.1 on 2022-08-22 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="review",
        ),
    ]
