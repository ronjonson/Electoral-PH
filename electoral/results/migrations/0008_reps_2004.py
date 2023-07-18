# Generated by Django 4.2.2 on 2023-07-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("electoral", "0007_remove_pres_2010_province_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reps_2004",
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
                ("electors", models.PositiveSmallIntegerField()),
                (
                    "province_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="electoral.province",
                    ),
                ),
            ],
        ),
    ]
