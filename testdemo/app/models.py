from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=50,default="")
    pan= models.CharField(max_length=50,default="")
    age = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name;
