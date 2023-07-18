from django.db import models
# Create your models here.


class Section(models.Model):   
    id_sect= models.AutoField(primary_key=True)
    sect_num= models.IntegerField(unique=True)

    def __str__(self):
        return str(self.sect_num)


class Group(models.Model):
    id_grp = models.AutoField(primary_key=True)
    grp_num=models.IntegerField()
    id_sect=models.ForeignKey(Section,on_delete=models.CASCADE)

    def __str__(self):
        return "grp: "+str(self.grp_num)+" sect: "+str(self.id_sect)