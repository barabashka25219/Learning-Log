from django.db import models
from django.contrib.auth.models import User

class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = 'userinfos'