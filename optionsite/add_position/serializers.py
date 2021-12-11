from rest_framework import serializers
from .models import Option


class OptionSerializer(serializers.Serializer):
    trade_id = serializers.IntegerField()
    symbol = serializers.CharField()
    strike = serializers.FloatField()
    expiration = serializers.DateField()
    type = serializers.CharField()
    bought = serializers.IntegerField()
    active = serializers.IntegerField()
    date_opened = serializers.DateField()

    class Meta:
        model = Option
        fields = ["trade_id", "symbol", "strike", "expiration", "type", "bought", "actives", "date_opened"]

    def create(self):
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
        )
        option.save()
        return option
