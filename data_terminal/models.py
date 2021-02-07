from django.db import models
# Create your models here.


class Data_Terminal(models.Model):
    SW = models.CharField(max_length=2)
    Status = models.IntegerField()
    TS = models.IntegerField()



