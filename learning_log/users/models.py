from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    firstname = models.CharField(max_length=128, blank=True)
    lastname = models.CharField(max_length=128, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='images/%Y%m%d', default='images/default/login.png')
    
    class Meta:
        verbose_name_plural = 'userinfos'
        
    @receiver(post_save, sender=User)
    def create_user_userinfo(sender, instance, created, **kwargs):
        if created:
            Userinfo.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_userinfo(sender, instance, created, **kwargs):
        instance.userinfo.save()