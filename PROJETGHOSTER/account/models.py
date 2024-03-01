from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User_app(models.Model):
    CREAOR ="CREATOR"
    SUBSCRIBER ="SUBSCRIIBER"
    
    ROLE_CHOICES =(
        (CREAOR,'Créateur'),
        (SUBSCRIBER,'Abonné')
    )
    
    profile_photo =models.ImageField(verbose_name="Photo de profil")
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    