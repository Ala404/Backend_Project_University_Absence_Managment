from django.db import models


# Create your models here.




class Classroom(models.Model):
    ROOMS=[('L','L'),('A','A'),('S','S')]
    
    classroom_id = models.AutoField(primary_key=True, editable=False,unique=True)
    classroom_code=models.IntegerField()
    classroom_type= models.CharField(max_length=2,choices=ROOMS, default='L',blank=True,unique=False)

    

    def __str__(self) :
        return self.classroom_type + str(self.classroom_code)