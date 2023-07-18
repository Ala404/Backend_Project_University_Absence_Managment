from django.db import models
from modules.models import Module
from sections.models import Section,Group
from classrooms.models import Classroom
from profs.models import Prof
# Create your models here.



class Schedule(models.Model):
    BOXES=[]
    for i in range(1,26):
        BOXES.append((i,i))
        
    TYPES=(('td','td'),('tp','tp'),('cours','cours'))
    
    id_sch= models.AutoField( unique=True, primary_key=True, editable=False)
    id_prof=models.ForeignKey(Prof,on_delete=models.CASCADE)
    id_mod=models.ForeignKey(Module,on_delete=models.CASCADE)
    sect_num=models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)
    grp_num= models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    type= models.CharField(choices= TYPES,max_length=5)
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    cell = models.IntegerField(choices= BOXES, unique=False)
    
    def __str__(self):
        return  "  id_sch:  "+str(self.id_sch)+ "  cell:  "+str(self.cell)+ "  type:  "+str(self.type)+ "  prof:  "+str(self.id_prof)+ "  mod:  "+str(self.id_mod)+ "  sect_num:  "+str(self.sect_num)+ "  grp_num:  "+str(self.grp_num)+ "  classroom:  "+str(self.classroom)