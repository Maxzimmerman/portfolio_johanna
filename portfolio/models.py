from django.db import models


# Create your models here.


class Home(models.Model):
    image = models.ImageField("Home bild", upload_to='home/')
    name = models.CharField("Name", max_length=30)
    job_role = models.CharField("Dein Jobbezeichnung", max_length=30)


class Header(models.Model):
    icon = models.ImageField(upload_to='home/')


class HeaderLinks(models.Model):
    name = models.CharField("Name", max_length=20)
    data_hover = models.CharField("Hovername", max_length=50, default=f"{name}")
    href = models.CharField("Link", max_length=50, default=f"#{name}")
    header = models.ForeignKey(Header, related_name="links", on_delete=models.CASCADE)
