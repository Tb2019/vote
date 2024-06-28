from django.db import models

# Create your models here.
from django.db import models

class Vote(models.Model):
    day = models.CharField(max_length=10)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.day
