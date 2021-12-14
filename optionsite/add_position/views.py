from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Option, Trade
from .serializers import OptionSerializer, TradeSerializer
from rest_framework import status
from datetime import date, timedelta

@api_view(["POST"])
def add_trade(request):
    '''
    Add a full trade strategy
    :param request: HTTP request with 'trade' fields
    :return: details of trade
    '''

    trade_id = len(Trade.objects.filter())+1

    data = {
        'id': trade_id,
        'strat': request.data.get('strat'),
        'open_date': date.today(),
        'symbol': request.data.get('symbol'),
        'spot': request.data.get('spot'),
        'iv': request.data.get('iv'),
        'ivr': request.data.get('ivr'),
        'open_price': request.data.get('open_price'),
        'expiration': date.today() + timedelta(request.data.get('dte')),
        'bpr': request.data.get('bpr'),
        'earnings': request.data.get('earnings'),
    }
    trade_serializer = TradeSerializer(data=data)
    if trade_serializer.is_valid():
        trade_serializer.create()
        return Response(trade_serializer.data, status=status.HTTP_201_CREATED)

    return Response(trade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def add_option(request):
    '''
    :param request: HTTP request with 'position' fields
    :return: details of position
    '''

    open_price = None
    single = request.data.get("single")

    if single:
        open_price = request.data.get('open_price')

    data = {
        'trade_id': request.data.get('trade_id'),
        'symbol': request.data.get('symbol'),
        'strike': request.data.get('strike'),
        'expiration': date.today() + timedelta(request.data.get('dte')),
        'type': request.data.get('type'),
        'bought': request.data.get('bought'),
        'active': 1,
        'date_opened': date.today(),
        'open_price': open_price,
    }
    position_serializer = OptionSerializer(data=data)
    if position_serializer.is_valid():
        position_serializer.create(single)
        return Response(position_serializer.data, status=status.HTTP_201_CREATED)

    return Response(position_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)