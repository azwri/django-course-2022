from django.db import models

class Flower(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()