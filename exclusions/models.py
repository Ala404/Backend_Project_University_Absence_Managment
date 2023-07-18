from django.db import models
import uuid
from students.models import Student
from modules.models import Module
# Create your models here.


class Exclusion(models.Model):
    id_exc= models.AutoField(unique=True,primary_key=True,editable=False)
    id_stud= models.ForeignKey(Student,on_delete=models.CASCADE)
    id_mod= models.ForeignKey(Module,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.id_exc)+' '+str(self.id_stud)+' '+str(self.id_mod)