# Generated by Django 4.2.6 on 2023-10-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes_app", "0005_alter_step_step_number_alter_step_step_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredients",
            name="ingr_unit",
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
    ]