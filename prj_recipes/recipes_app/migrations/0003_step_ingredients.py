# Generated by Django 4.2.6 on 2023-10-29 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes_app", "0002_alter_category_categ_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="Step",
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
                ("step_number", models.CharField(max_length=100)),
                ("step_text", models.FloatField()),
                (
                    "step_rec",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes_app.recipe",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ingredients",
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
                ("ingr_name", models.CharField(max_length=100)),
                ("ingr_amount", models.FloatField()),
                (
                    "ingr_rec",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes_app.recipe",
                    ),
                ),
            ],
        ),
    ]