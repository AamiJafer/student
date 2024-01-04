from django.db import models

class studentRegister(models.Model):
    name=models.CharField(max_length=255,null=True)
    address=models.TextField(null=True)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    joiningDate=models.DateField(null=True)
    qualification=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=255,null=True)
    mobile=models.CharField(max_length=255,null=True)
    password=models.CharField(max_length=255,null=True)
# Create your models here.
