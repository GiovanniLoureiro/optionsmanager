from rest_framework import serializers
from .models import Option


class OptionSerializer(serializers.Serializer):
    symbol = serializers.CharField()
    strike = serializers.FloatField()
    type = serializers.CharField()

    class Meta:
        model = Option
        fields = ["symbol", "strike", "type"]

    def create(self):
        '''
        creates a option object with necessary fields
        '''
        option = Option(
            symbol=self.validated_data['symbol'],
            strike=self.validated_data['strike'],
            type=self.validated_data['type'],
        )
        option.save()
        return option
