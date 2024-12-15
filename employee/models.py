from django.db import models

# Create your models here.

class Employees(models.Model):
    fname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=12,blank=True)
    photo=models.ImageField(upload_to="images")
    creted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.fname+" "+self.lastname 
    
