from django.db import models
from grouplist.models import Groups

class Schedule(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    date = models.DateField()
    memo = models.CharField(max_length=200)