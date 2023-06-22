from django.db import models

# Create your models here.
class Student(models.Model):
    admission_no = models.IntegerField(unique=True)

    full_name = models.CharField(max_length=50)

    email = models.EmailField(max_length=100)

    age = models.IntegerField()

    CLASS_CHOICES = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('11', '11th'),
        ('12', '12th'),
    )
    class_level = models.CharField(max_length=2, choices=CLASS_CHOICES)

    description = models.TextField()

    image = models.ImageField(upload_to='images/')

    marklist = models.FileField(upload_to='marklists/')

    def __str__(self):
        return self.full_name