from django.db import models

# Create your models here.

class employee_model(models.Model):
    employee_name=models.CharField(max_length=20)
    employee_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.employee_name
    
