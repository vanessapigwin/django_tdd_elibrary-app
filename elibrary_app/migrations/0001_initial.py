# Generated by Django 4.2 on 2023-05-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Catalogue",
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
                ("title", models.CharField(max_length=255)),
                ("ISBN", models.CharField(max_length=20)),
                ("author", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "availability",
                    models.CharField(
                        choices=[("true", "True"), ("false", "False")], max_length=5
                    ),
                ),
            ],
        ),
    ]
