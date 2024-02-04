from django.db import models

# Create your models here.


class Home(models.Model):
    image = models.ImageField(upload_to='home/')
    name = models.CharField(max_length=30)
    job_role = models.CharField(max_length=30)
