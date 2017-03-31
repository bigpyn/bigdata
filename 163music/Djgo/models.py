from django.db import models

# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=50,null=False,unique=True)
    password=models.CharField(max_length=50,null=False,unique=True)
    Email=models.CharField(max_length=50,null=False,unique=True)
    def __str__(self):
        return self.username


