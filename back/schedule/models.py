from django.db import models
from datetime import date

# Create your models here.

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    start = models.DateTimeField((), default=date.today)
    end = models.DateTimeField((), default=date.today)
    allDay = models.BooleanField(default=False)

    def _str_(self):
        return self.title