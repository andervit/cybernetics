from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250)
    chef = models.ForeignKey('Professor', null=True, blank=True,related_name='chef')
    short_info = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    domen = models.CharField(max_length=150)
    specialization = models.ForeignKey('Specialization', null=True, blank=True)

    def __str__(self):
        return name

class Professor(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, null=True, blank=True)
    position = models.CharField(max_length=250)
    interest = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    domen = models.CharField(max_length=150)
    detail = models.TextField(null=True, blank=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Administration(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    domen = models.CharField(max_length=150)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)
    pub_date = models.DateField()
    photo = models.ImageField(null=True, upload_to="img")
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class CustomUser(User):
    department = models.ForeignKey(Department, null=True, blank=True)

    def cheak_permision(self, department):
        return self.department == department


class Photo(models.Model):
    alt = models.CharField(max_length=250)
    photo = models.ImageField()
    def __str__ (self):
        return self.alt

class Article(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)
    image = models.ManyToManyField(Photo, null=True, blank=True)
    slug = models.CharField(max_length=250)

    def __str__ (self):
        return self.title
