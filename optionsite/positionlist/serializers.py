from rest_framework import serializers
from .models import Option


class OptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    symbol = serializers.CharField()
    strike = serializers.FloatField()
    type = serializers.CharField()

    class Meta:
        model = Option
        fields = ["id", "symbol", "strike", "type"]

