from django.db import models

class NewUser(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
    website = models.CharField(max_length = 100)