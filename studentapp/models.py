from django.db import models
from datetime import date





class Employee(models.Model):
    firstname = models.CharField(max_length=50,blank=False,null=False)
    lastname = models.CharField(max_length=50,blank=False,null=False)
    SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
    semester = models.CharField(choices=SEMESTER_CHOICES,max_length=100)
    age = models.IntegerField(blank=False,null=False)
    department = models.CharField(max_length=100,blank=False,null=False)
    OrganizationID = models.BigIntegerField(default=0)
    CreatedBy = models.BigIntegerField(default=0)
    CreatedDateTime = models.DateField(default = date.today)
    ModifyBy = models.BigIntegerField(default=0)
    ModifyDateTime = models.DateField(default = date.today)
    IsDelete = models.BooleanField(default=False) 


        

    def __str__(self):
        return self.firstname
    
    
  