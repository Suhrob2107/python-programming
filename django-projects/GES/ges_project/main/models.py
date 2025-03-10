from tkinter.font import names

from django.db import models

# Create your models here.

class Filial(models.Model):
    title = models.CharField(max_length=300)
    status = models.IntegerField(default=0)
    address = models.CharField(max_length=300,blank=True)
    phone = models.CharField(max_length=300,blank=True)
    instagram = models.CharField(max_length=300,blank=True)
    whatsapp = models.CharField(max_length=300,blank=True)
    email = models.CharField(max_length=300,blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Register(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    filial = models.ForeignKey(Filial,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=600)
    description = models.TextField()
    status = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='upload',blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Prize(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=600)
    description = models.TextField()
    status = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='upload',blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Information(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=600,blank=True)
    description = models.TextField()
    status = models.IntegerField(default=0)
    video_link = models.CharField(max_length=300,blank=True)
    facebook = models.CharField(max_length=300,blank=True)
    whatsapp = models.CharField(max_length=300,blank=True)
    youtube = models.CharField(max_length=300,blank=True)
    instagram = models.CharField(max_length=300,blank=True)
    telegram = models.CharField(max_length=300,blank=True)
    phone = models.CharField(max_length=300,blank=True)
    email = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.title


class Staff(models.Model):
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=600)
    description = models.TextField()
    position = models.CharField(max_length=600)
    status = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='upload',blank=True)
    filial = models.ForeignKey(Filial,on_delete=models.CASCADE)
    subject = models.CharField(max_length=600)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name


class Vacancy(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='upload',blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title