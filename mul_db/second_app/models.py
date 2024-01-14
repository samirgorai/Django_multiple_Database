from django.db import models

# Create your models here.

class Student_model(models.Model):
    student_name=models.CharField(max_length=20)
    student_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.student_name