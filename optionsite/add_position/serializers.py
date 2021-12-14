from rest_framework import serializers
from .models import Option, Trade


class TradeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    strat = serializers.CharField()
    open_date = serializers.DateField()
    symbol = serializers.CharField()
    spot = serializers.FloatField()
    iv = serializers.FloatField()
    ivr = serializers.FloatField()
    open_price = serializers.FloatField()
    expiration = serializers.DateField()
    bpr = serializers.FloatField()
    earnings = serializers.BooleanField()

    class Meta:
        model = Trade
        fields = ["id", "open_date", "symbol", "spot", "iv", "ivr", "open_price",  "expiration", "bpr", "earnings"]

    def create(self):
        '''
        creates a trade object with required option fields
        '''
        trade = Trade(
            id=self.validated_data["id"],
            strat=self.validated_data["strat"],
            open_date=self.validated_data['open_date'],
            symbol=self.validated_data['symbol'],
            spot=self.validated_data['spot'],
            iv=self.validated_data['iv'],
            ivr=self.validated_data['ivr'],
            open_price=self.validated_data['open_price'],
            expiration=self.validated_data['expiration'],
            bpr=self.validated_data['bpr'],
            earnings=self.validated_data['earnings']
        )
        trade.save()
        return trade


class OptionSerializer(serializers.Serializer):
    trade_id = serializers.IntegerField()
    symbol = serializers.CharField()
    strike = serializers.FloatField()
    expiration = serializers.DateField()
    type = serializers.CharField()
    bought = serializers.IntegerField()
    active = serializers.IntegerField()
    date_opened = serializers.DateField()
    open_price = serializers.FloatField()

    class Meta:
        model = Option
        fields = ["trade_id", "symbol", "strike", "expiration", "type", "bought", "actives", "date_opened", "open_price"]

    def create(self, single):
        '''
        creates a option object with necessary fields
        '''
        option = Option(
            trade_id=self.validated_data['trade_id'],
            symbol=self.validated_data['symbol'],
            strike=self.validated_data['strike'],
            expiration=self.validated_data['expiration'],
            type=self.validated_data['type'],
            bought=self.validated_data['bought'],
            active=self.validated_data['active'],
            date_opened=self.validated_data['date_opened'],
            open_price=self.validated_data['open_price']
        )
        option.save()
        return option
