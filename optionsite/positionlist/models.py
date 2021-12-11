from django.db import models


class Option(models.Model):
    id = models.BigAutoField(primary_key=True)
    symbol = models.CharField(max_length=5)
    strike = models.FloatField()
    type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'option'
