from django.db import models
from absences.models import Absence
# Create your models here.



class Justification(models.Model): 
    STATUS = (("accepted","accepted"),("refused","refused"),("hold","hold"))
    
    
    id_just= models.AutoField(unique=True,primary_key=True,editable=False)
    just_doc = models.ImageField(upload_to='justifications/',null=True,blank=True, default='justifications/default.jpg')
    status = models.CharField(choices=STATUS,max_length=10,default="hold")
    id_abs=models.ForeignKey(Absence,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return "id_jst: "+str(self.id_just)+' id_abs: '+str(self.id_abs)+' sts: '+str(self.status)