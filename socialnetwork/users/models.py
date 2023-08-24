from django.db import models

class Profile(models.Model):
    user = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    interests = models.TextField()
    def __str__(self):
        return self.name
