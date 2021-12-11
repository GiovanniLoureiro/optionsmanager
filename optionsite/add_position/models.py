from django.db import models


class Option(models.Model):
    id = models.BigAutoField(primary_key=True)
    trade_id = models.BigIntegerField()
    symbol = models.CharField(max_length=5)
    strike = models.FloatField()
    expiration = models.DateField()
    type = models.CharField(max_length=4)
    bought = models.IntegerField()
    active = models.IntegerField()
    date_opened = models.DateField()

    class Meta:
        managed = False
        db_table = 'option'
