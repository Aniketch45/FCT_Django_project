from django.db import models
# Create your models here.

class Stud(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.sname
    
class Stud2(models.Model):
    snm = models.CharField(max_length=50)
    semail = models.EmailField()

    def __str__(self):
        return self.snm
    

    
