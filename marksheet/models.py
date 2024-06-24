from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class markupdate(models.Model):
    rollno=models.CharField(unique=True,max_length=10)
    name=models.CharField(max_length=100)
    sub1=models.CharField(max_length=25)
    mark1=models.IntegerField(validators=[MaxValueValidator(100)])
    sub2=models.CharField(max_length=25)
    mark2=models.IntegerField(validators=[MaxValueValidator(100)])
    sub3=models.CharField(max_length=25)
    mark3=models.IntegerField(validators=[MaxValueValidator(100)])
    sub4=models.CharField(max_length=25)
    mark4=models.IntegerField(validators=[MaxValueValidator(100)])
    sub5=models.CharField(max_length=25)
    mark5=models.IntegerField(validators=[MaxValueValidator(100)])
    sub6=models.CharField(max_length=25)
    mark6=models.IntegerField(validators=[MaxValueValidator(100)])


    