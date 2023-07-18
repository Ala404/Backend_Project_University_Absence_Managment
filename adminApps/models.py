from django.db import models
import uuid
from profiles.models import Profile
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver



# Create your models here.



class Admin(models.Model):
   
    id = models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False) 
    first_name= models.CharField(max_length=32,blank=True)
    last_name= models.CharField(max_length=32,blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) :
        return self.first_name + " " + self.last_name



     

        

