# Generated by Django 4.2.6 on 2023-10-14 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wait_list_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Med_org",
            new_name="MedOrgMod",
        ),
        migrations.RenameModel(
            old_name="ReportBeds",
            new_name="ReportBedsMod",
        ),
    ]
