from django.db import models
import uuid
from sessionApps.models import Session
from students.models import Student
# Create your models here.


class Absence(models.Model):
    id_abs = models.AutoField(unique=True,primary_key=True,editable=False)
    id_sess=models.ForeignKey(Session,on_delete=models.CASCADE)
    id_stud=models.ForeignKey(Student,on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id_abs)+' '+str(self.id_sess)+' '+str(self.id_stud)