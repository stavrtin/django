# Generated by Django 4.2.6 on 2023-10-14 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wait_list_app", "0003_rename_name_meg_org_reportbedsmod_meg_org"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reportbedsmod",
            old_name="meg_org",
            new_name="med_org",
        ),
    ]