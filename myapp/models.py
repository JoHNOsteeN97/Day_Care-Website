from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
        ph_number=models.BigIntegerField(default=0)
        place=models.CharField(max_length=15,null=True)
        address=models.CharField(max_length=30,null=True)
        id_proof=models.CharField(max_length=30,null=True)
        occupation=models.CharField(max_length=15,null=True)
        qualification=models.CharField(max_length=25,null=True)
        salary=models.FloatField(default=0)
        dob=models.DateField(null=True)
        resume=models.FileField(default=0)
        caretaker_status=models.IntegerField(default=0)
        usertype=models.IntegerField(default=0)
        
        
        
        
class Children(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    age=models.IntegerField()
    parent_id=models.IntegerField(null=True)
    caretaker_id=models.IntegerField(null=True,default=0)
    blood_group=models.CharField(max_length=30)
    medical_condition=models.TextField(max_length=300)
    

class Message(models.Model):
        ename=models.CharField(max_length=30)
        email=models.EmailField(max_length=50)
        msg=models.TextField(max_length=500)
        type=models.IntegerField(default=0)
                
    
class Appointment(models.Model):
        child_id=models.IntegerField(null=True)
        date_app=models.DateTimeField()
        app_status=models.IntegerField(default=0)
        
        
        
        
        
        