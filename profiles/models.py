import json
from django.db import models
import uuid






# Create your models here.



class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,default=uuid.uuid4)
    TYPES = [('admin','admin'),('prof','prof'),('student','student')]
   
    id_profile = models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)
    user_name= models.CharField(max_length=32,editable=True)
    email = models.EmailField(max_length=64, blank =True, null=True)
    password = models.CharField(max_length=32,null= True, blank =True)
    profile_type = models.CharField(max_length=50, choices = TYPES, default='student')
    
    
    def __str__(self):
        return str(self.user_name)
    
    # def get_all_data(self):
    #     return{"user_name":self.user_name,"email": self.email,"password": self.password,"profile_type": self.profile_type}
    



       




