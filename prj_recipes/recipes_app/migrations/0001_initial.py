# Generated by Django 4.2.6 on 2023-10-29 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
            ],
        ),
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
                ("categ_name", models.CharField(max_length=100)),
                ("categ_description", models.CharField(max_length=100)),
                ("categ_img", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                ("rec_name", models.CharField(max_length=100)),
                ("rec_description", models.CharField(max_length=100)),
                ("rec_how_do", models.TextField()),
                ("rec_time", models.IntegerField()),
                ("rec_img", models.ImageField(upload_to="")),
                (
                    "rec_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes_app.author",
                    ),
                ),
                (
                    "rec_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes_app.category",
                    ),
                ),
            ],
        ),
    ]