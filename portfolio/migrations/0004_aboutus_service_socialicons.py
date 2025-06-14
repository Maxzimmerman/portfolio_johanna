# Generated by Django 4.2.9 on 2024-02-07 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0003_alter_headerlinks_header"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=30, verbose_name="Titel")),
                ("image", models.ImageField(upload_to="about/", verbose_name="Über dich Bild")),
                ("text", models.TextField(verbose_name="Text")),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="about/service/", verbose_name="Angebot Bild")),
                ("title", models.CharField(max_length=30, verbose_name="Titel")),
                ("text", models.TextField(verbose_name="Text")),
                ("more_information", models.TextField(verbose_name="Mehr Informationen")),
            ],
        ),
        migrations.CreateModel(
            name="SocialIcons",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=20, verbose_name="Name")),
                ("class_name", models.CharField(max_length=30, verbose_name="Klassenname")),
                ("href", models.TextField(verbose_name="Link")),
                (
                    "about_us",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="icons", to="portfolio.aboutus"
                    ),
                ),
            ],
        ),
    ]
