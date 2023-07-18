from django.db import models
import uuid
# Create your models here.


class Module(models.Model):
    id_mod = models.AutoField( unique=True,primary_key=True,editable=False)
    mod_name =models.CharField(max_length=32,unique=True)

    def __str__(self):
     return self.mod_name
    
    # def get_all_data(self):
    #     return {"id_mod":self.id_mod,"mod_name": self.mod_name}