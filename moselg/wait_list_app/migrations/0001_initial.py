# Generated by Django 4.2.6 on 2023-10-14 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Med_org",
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
                ("name", models.CharField(max_length=150)),
                ("type", models.CharField(max_length=150)),
                ("on_activ", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="ReportBeds",
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
                ("m_employ", models.IntegerField()),
                ("f_employ", models.IntegerField()),
                ("m_free", models.IntegerField()),
                ("f_free", models.IntegerField()),
                (
                    "name_meg_org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wait_list_app.med_org",
                    ),
                ),
            ],
        ),
    ]