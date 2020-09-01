from django.db import models

class User_Details(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.TextField()
    user_email = models.EmailField()
    profile_pic = models.ImageField()

class Content(models.Model):
    pass
