from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings 




class UserProfileManager(BaseUserManager):
    """User Manager Profile"""

    def create_user(self,email,name,password=None):
        """Crée un nouveau user"""
        if not email:
            raise ValueError('Un User doit avoir un email')
        if not name:
            raise ValueError('Un nom est obligatoire')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)

      
        user.save(using=self._db)

        return user
    def create_superuser(self, email,name, password):
        """crée un superuser"""

        user=self.create_user(email,name, password)
        
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Notre modèle pour les utilsateurs du système"""

    email = models.EmailField(max_length=254, unique=True)
    name=models.CharField(max_length=50,unique=True)
    is_activate=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)    

    USERNAME_FIELD = 'email'
    REQUIRED_FILEDS= ['name']

    objects = UserProfileManager()

    def get_full_name(self):
        """Renvoi le nom complet de l'utilisateur"""

        return self.name
    def get_short_name(self):
        """Renvoi Short nom du user"""
        
        return self.name
    
    def __str__(self):
        return self.email
    

class ProfileFeedItem(models.Model):
    """Profile Status"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True) 
        
    def __str__(self):
        """Retourne le modèle comme String"""
        return self.status_text
        