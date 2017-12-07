"""Creates the data fields in the profile model in the database"""
from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    """Specifies the data fields in the profile model in the database"""
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    cost = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """Allows for a dataset to be reffered by the value given as the name"""
        return self.name
