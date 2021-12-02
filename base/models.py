from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    brief_desc = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="Images/services/")


    def __str__(self):
        return self.title


class Testimony(models.Model):
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=60)
    comment = models.CharField(max_length=130)


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural="Testimonies"

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
    
    