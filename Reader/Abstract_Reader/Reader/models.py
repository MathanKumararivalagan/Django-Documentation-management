from django.db import models

# Create your models here.
class Student(models.Model):
    image=models.ImageField(upload_to="Media/Student_img",null=True)
    project=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    batch=models.IntegerField(max_length=5,null=True)
    abstract=models.CharField(max_length=5000,null=True)
    link=models.CharField(max_length=500,null=True)
    
    
    
    def __str__(self):
        return self.rollno+" - "+self.name
    