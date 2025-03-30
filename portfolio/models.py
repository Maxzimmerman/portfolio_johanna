from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='images')
    image = models.ImageField("Portfolio Bild", upload_to='portfolio/')

    def __str__(self):
        return "Portfolio Image"


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
    slug = models.SlugField("Slug", default=f"{title}")

    def get_absolute_url(self):
        return reverse("service_detail", args=[self.slug])

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField("Title", max_length=30, default="Konkaktieren Sie mich")
    address = models.CharField("Adresse", max_length=50)
    email = models.CharField("Email", max_length=40)
    phone = models.CharField("Telefonnummer", max_length=30)

    def __str__(self):
        return "Kontaktformular"


class Form(models.Model):
    title = models.CharField("Form Titel", max_length=40)
    button_text = models.CharField("Form Button", max_length=30)
    name_type = models.CharField("Feld Typ", max_length=30)
    name_name = models.CharField("Feld Name", max_length=30)
    name_id = models.CharField("Feld Id", max_length=30)
    name_placeholder = models.CharField("Feld Placeholder", max_length=40)
    email_type = models.CharField("Feld Typ", max_length=30)
    email_name = models.CharField("Feld Name", max_length=30)
    email_fiel_id = models.CharField("Feld Id", max_length=30)
    email_placeholder = models.CharField("Feld Placeholder", max_length=40)
    message_name = models.CharField("Feld Name", max_length=30)
    message_fiel_id = models.CharField("Feld Id", max_length=30)
    message_placeholder = models.CharField("Feld Placeholder", max_length=40)
    contact = models.ForeignKey("Contact", related_name="forms", on_delete=models.CASCADE)

    def __str__(self):
        return self.name_name


class SocialIconsContact(models.Model):
    name = models.CharField("Name", max_length=20)
    class_name = models.CharField("Klassenname", max_length=30)
    href = models.TextField("Link")
    contact = models.ForeignKey("Contact", related_name="icons", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Footer(models.Model):
    icon = models.ImageField(upload_to='footer/')
    copy_right = models.CharField("Copyright", max_length=30)

    def __str__(self):
        return f"Copryright: {self.copy_right}"


class TextSection(models.Model):
    header = models.CharField("Überschrift", max_length=40)
    text = models.TextField("Text")


class Imprint(models.Model):
    company_name = models.CharField("Firmenname", max_length=50)
    owner_name = models.CharField("Name der Geschäftsführerin", max_length=60)
    street_name = models.CharField("Straße", max_length=100)
    house_number = models.CharField("Hausnummer", max_length=10)
    postel_code = models.CharField("Postleitzahl", max_length=6)
    city = models.CharField("Stadt", max_length=40, default="Frankfurt")
    represented_by = models.CharField("Vertreten durch", max_length=60)
    phone = models.CharField("Telefonnummer", max_length=20)
    email = models.CharField("E-Mail", max_length=30)
    tax_number = models.CharField("Steuernummer", max_length=11, default=00000000000)
