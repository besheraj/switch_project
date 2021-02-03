from django.db import models
# Create your models here.


class data_terminal(models.Model):
    SW = models.CharField(max_length=2)
    T1 = models.IntegerField()
    T2 = models.IntegerField()
    T3 = models.IntegerField()
    T4 = models.IntegerField()
    T5 = models.IntegerField()
    TS = models.IntegerField()

