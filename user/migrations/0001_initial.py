# Generated by Django 5.1.5 on 2025-01-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("avatar", models.ImageField(upload_to="avatars")),
                (
                    "level",
                    models.CharField(
                        choices=[("JR", "Junior"), ("ME", "Middle"), ("SR", "Senior")],
                        default="JR",
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
