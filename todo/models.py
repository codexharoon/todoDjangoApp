from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=1000000)
    complete = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now(),blank=True)
    userid = models.IntegerField()

    def __str__(self):
        return self.title
