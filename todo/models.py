from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(blank=True, max_length=100)  # Corrected line
    user = models.ForeignKey(User, on_delete=models.CASCADE)
