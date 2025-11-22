from django.db import models


class Employees(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    image = models.ImageField(upload_to='images')
    Department = models.CharField(max_length=40)
    Designation = models.CharField(max_length=50)
    Location = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, unique=True)
    # blank to make it optional field
    contact_no = models.CharField(max_length=13, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(default="No description provided")

    def __str__(self):
        return self.Name

