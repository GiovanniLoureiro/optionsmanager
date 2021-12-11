from django.db import models


class Option(models.Model):
    symbol = models.CharField(max_length=4)
    strike = models.FloatField()
