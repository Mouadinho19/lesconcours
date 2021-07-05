from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='nom d\'utulisateur')
    city = ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, null=True, blank=True, verbose_name='ville')
    phone_number = CharField(max_length=15, verbose_name='numero de telephone')
    image = ImageField(upload_to='profile/',blank=True, null=True)
    class Meta:
        verbose_name_plural = "profil"
    
    def __str__(self):
        return str(self.user)
        
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class City(models.Model):
    name = CharField(max_length=30, verbose_name='nom')

    class Meta:
        verbose_name_plural = "ville"

    def __str__(self):
        return self.name