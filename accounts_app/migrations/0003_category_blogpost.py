# Generated by Django 4.1.6 on 2024-07-06 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts_app", "0002_alter_customuser_groups_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="blog_images/")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Mental Health", "Mental Health"),
                            ("Heart Disease", "Heart Disease"),
                            ("Covid19", "Covid19"),
                            ("Immunization", "Immunization"),
                        ],
                        max_length=100,
                    ),
                ),
                ("summary", models.TextField()),
                ("content", models.TextField()),
                ("draft", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
