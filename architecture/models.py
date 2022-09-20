import email
from email import message
from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=400)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image1 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    image2 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    image3 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    image4 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    image5 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    image6 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    date = models.DateField()

class AboutMe(models.Model):
    my_description = models.TextField(max_length=1500)
    my_image = models.ImageField(null=True, blank=True,  upload_to = 'images')

class AboutUs(models.Model):
    company_description = models.TextField(max_length=1500)
    company_image = models.ImageField(null=True, blank=True,  upload_to = 'images')

class SliderImage(models.Model):
    slider_image1 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    slider_image2 = models.ImageField(null=True, blank=True,  upload_to = 'images')
    slider_image3 = models.ImageField(null=True, blank=True,  upload_to = 'images')



