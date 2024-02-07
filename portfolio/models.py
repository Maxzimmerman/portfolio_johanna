from django.db import models


# Create your models here.


class Home(models.Model):
    image = models.ImageField("Home bild", upload_to='home/')
    name = models.CharField("Name", max_length=30)
    job_role = models.CharField("Dein Jobbezeichnung", max_length=30)


class Header(models.Model):
    icon = models.ImageField(upload_to='home/')

    def __str__(self):
        return "Logo"


class HeaderLinks(models.Model):
    name = models.CharField("Name", max_length=20)
    data_hover = models.CharField("Hovername", max_length=50)
    href = models.CharField("Link", max_length=50)
    header = models.ForeignKey("Header", related_name="links", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class AboutUs(models.Model):
    title = models.CharField("Titel", max_length=30)
    image = models.ImageField("Über dich Bild", upload_to='about/')
    text = models.TextField("Text")

    def __str__(self):
        return self.title


class SocialIcons(models.Model):
    name = models.CharField("Name", max_length=20)
    class_name = models.CharField("Klassenname", max_length=30)
    href = models.TextField("Link")
    about_us = models.ForeignKey("AboutUs", related_name="icons", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    image = models.ImageField("Angebot Bild", upload_to='about/service/')
    title = models.CharField("Titel", max_length=30)
    text = models.TextField("Text")
    more_information = models.TextField("Mehr Informationen")

    def __str__(self):
        return self.title
