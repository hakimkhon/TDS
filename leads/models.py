import profile
from pyexpat import model
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_ustoz = models.BooleanField(default=True)

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user.username)

class Lead(models.Model):
    ism = models.CharField(max_length=15)
    famila = models.CharField(max_length=15)
    yosh = models.IntegerField(default=0)
    qiziqishi = models.CharField(max_length=100)
    tulov = models.BooleanField(default=False)
    organisation = models.ForeignKey(UserProfil, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.ism)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfil, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

def post_user_saqlash(sender, instance, created, **kwargs):
    if created:
        UserProfil.objects.create(user = instance)

post_save.connect(post_user_saqlash, sender = User)
