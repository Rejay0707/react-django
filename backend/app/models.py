from django.db import models

# Create your models here.
class React(models.Model):
    employee = models.CharField(max_length=30)  # Removed the comma
    department = models.CharField(max_length=200,default="Default Department")  # Removed the comma

    def __str__(self):
        return self.employee  # Optional: Make debugging easier
