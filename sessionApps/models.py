from datetime import timezone
from django.db import models
import uuid
from modules.models import Module
from sections.models import Section,Group
from schedules.models import Schedule
from profs.models import Prof
from classrooms.models import Classroom
# Create your models here.


class Session(models.Model):
    TYPES=(('td','td'),('tp','tp'),('cour','cour'))
    
    
    id_sess= models.AutoField(unique=True,primary_key=True,editable=False)
    # schedule= models.ForeignKey(Schedule, on_delete=models.CASCADE)
    id_prof=models.ForeignKey(Prof,on_delete=models.CASCADE)
    id_mod=models.ForeignKey(Module,on_delete=models.CASCADE)
    sect_num=models.ForeignKey(Section,on_delete=models.CASCADE)
    grp_num= models.ForeignKey(Group,on_delete=models.CASCADE)
    sess_type= models.CharField(choices= TYPES,max_length=5,default='cour')
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    date = models.DateTimeField(unique=False)
    created_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return 'id_sess: '+str(self.id_sess)+"  "+str(self.id_mod)+"  "+str(self.id_prof)+" sect: "+str(self.sect_num)+"  "+str(self.grp_num)+" "+str(self.sess_type)+" class"+str(self.classroom)+" "+str(self.date)+" "+str(self.created_date)
    



# class SessionDate (models.Model):
#     id_date = models.AutoField(unique=True,primary_key=True,editable=False)
#     sess_date= 
    
#     def __str__(self):
#         return 'id_dte:'+str(self.id_date)+" "+str(self.sess_date)