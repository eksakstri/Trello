from django.db import models
from django.db.models import Model

# Create your models here.

class users(models.Model):
    Username = models.CharField(max_length=50)
    Usertype = models.IntegerField(default=0)

class projects(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=400)
    Status = models.CharField(max_length=20)
    Duedate = models.DateField()
    Member = models.ManyToManyField(users)

class lists(models.Model):
    Name = models.CharField(max_length=20)
    Under_Project = models.ForeignKey(projects, on_delete=models.CASCADE)

class cards(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=400)
    Status = models.CharField(max_length=20)
    Duedate = models.DateField()
    Under_Project = models.ForeignKey(projects, on_delete=models.CASCADE)
    Under_List = models.ForeignKey(lists, on_delete=models.CASCADE)

