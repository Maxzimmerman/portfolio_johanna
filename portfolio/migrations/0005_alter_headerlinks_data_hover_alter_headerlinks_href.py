# Generated by Django 4.2.9 on 2024-02-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0004_aboutus_service_socialicons"),
    ]

    operations = [
        migrations.AlterField(
            model_name="headerlinks",
            name="data_hover",
            field=models.CharField(max_length=50, verbose_name="Hovername"),
        ),
        migrations.AlterField(
            model_name="headerlinks",
            name="href",
            field=models.CharField(max_length=50, verbose_name="Link"),
        ),
    ]
