from django.db import models
from django.db.models import Model


class Fan(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Student(models.Model):
    familya=models.CharField(max_length=50)
    ismi=models.CharField(max_length=50)
    otasini_ismi=models.CharField(max_length=50)
    tel_raqami=models.CharField(max_length=50)
    adres=models.CharField(max_length=100)
    fan=models.ForeignKey(Fan,on_delete=models.CASCADE)
    def __str__(self):
        return self.ismi
