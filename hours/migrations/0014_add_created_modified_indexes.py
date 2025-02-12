# Generated by Django 3.2 on 2021-04-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hours", "0013_split_user_editable_field"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="dateperiod",
            index=models.Index(
                fields=["created"], name="hours_datep_created_79f827_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dateperiod",
            index=models.Index(
                fields=["modified"], name="hours_datep_modifie_c821d2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="resource",
            index=models.Index(
                fields=["created"], name="hours_resou_created_5c5b92_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="resource",
            index=models.Index(
                fields=["modified"], name="hours_resou_modifie_e2851b_idx"
            ),
        ),
    ]
