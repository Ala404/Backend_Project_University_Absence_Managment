from django.db import models
import uuid
from modules.models import Module
from profiles.models import Profile
# Create your models here.



class Prof(models.Model):
    S= [('male','male'),('female','female')]
    
    id_prof = models.UUIDField( default=uuid.uuid4 , unique=True, primary_key=True, editable=False) 
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    module = models.ManyToManyField(Module)
    sex= models.CharField(max_length=10, choices=S , null=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
     return self.first_name+' '+self.last_name