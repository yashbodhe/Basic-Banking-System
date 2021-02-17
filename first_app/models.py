from django.db import models

# Create your models here.


class User(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    ebal=models.FloatField()
    
    def __str__(self):
        return 'Customer Object with eno: ' +str(self.eno) 
