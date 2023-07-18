from django.db import models
import uuid
from sections.models import Section, Group
from profiles.models import Profile
# Create your models here.


class Student(models.Model):
    S=(('male','male'),('female','female'))
    
    id_stud= models.UUIDField(unique=True,primary_key=True,editable=False,default=uuid.uuid4)
    first_name=models.CharField(max_length=32,blank=True)
    last_name=models.CharField(max_length=32,blank=True) 
    reg_num=models.IntegerField(null=True, blank=True)
    sex=models.CharField(null=True,blank=True,choices= S ,max_length=50)
    birth=models.DateField(null=True, blank=True)
    sect_num=models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)
    grp_num=models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
     return str(self.first_name)+" "+str(self.last_name)+" N_reg: "+str(self.reg_num) +"  "+str(self.grp_num)