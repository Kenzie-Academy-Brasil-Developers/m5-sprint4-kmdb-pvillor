# Generated by Django 4.1 on 2022-08-19 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stars", models.IntegerField()),
                ("review", models.TextField()),
                ("spoilers", models.BooleanField(default=False)),
                (
                    "recomendation",
                    models.CharField(
                        choices=[
                            ("Must Watch", "Must Watch"),
                            ("Should Watch", "Should Watch"),
                            ("Avoid Watch", "Avoid Watch"),
                            ("No Opinion", "Default"),
                        ],
                        default="No Opinion",
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
