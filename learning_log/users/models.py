from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    firstname = models.CharField(max_length=128, blank=True)
    lastname = models.CharField(max_length=128, blank=True)
    
    class Meta:
        verbose_name_plural = 'userinfos'
        
    # @receiver(post_save, sender=User)
    # def create_info(sender, instance, created, **kwargs):
    #     if created:
    #         Userinfo.objects.create(user=instance)
            
    # @receiver(post_save, sender=User)
    # def save_info(sender, instance, created, **kwargs):
    #     instance.userinfo.save()