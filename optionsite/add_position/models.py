from django.db import models


class Trade(models.Model):
    id = models.BigAutoField(primary_key=True)
    strat = models.CharField(max_length=30)
    open_date = models.DateField()
    symbol = models.CharField(max_length=5)
    spot = models.FloatField()
    iv = models.FloatField()
    ivr = models.FloatField()
    bpr = models.FloatField()
    expiration = models.DateField()
    open_price = models.FloatField()
    earnings = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'trade'


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
    open_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'option'
