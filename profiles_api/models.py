from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager




class UserProfileManager(BaseUserManager):
    """User Manager Profile"""

    def create_user(self,email,name,password=None):
        """Crée un nouveau user"""
        if not email:
            raise ValueError('Un User doit avoir un email')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)

        user.save(usinf=self._db)

        return user
    def create_superuser(self, email,name, password):
        """crée un superuser"""

        user=self.create_user(email,name, password)
        
        user.is_superuser= True 
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Notre modèle pour les utilsateurs du système"""

    email = models.EmailField(max_length=254, unique=True)
    name=models.CharField(max_length=50)
    is_activate=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FILEDS= ['name']

    def get_full_name(self):
        """Renvoi le nom complet de l'utilisateur"""

        return self.name
    def get_short_name(self):
        """Renvoi Short nom du user"""
        
        return self.name
    
    def __str__(self):
        return self.email
    




