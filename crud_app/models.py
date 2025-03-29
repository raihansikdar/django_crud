from django.db import models

class PersonModel(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    cgpa = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

