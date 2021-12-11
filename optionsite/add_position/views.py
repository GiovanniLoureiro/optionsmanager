from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Option
from .serializers import OptionSerializer
from rest_framework import status
from datetime import date, timedelta


@api_view(["GET"])
def list_all_positions(request):
    '''
    lists all options positions
    :param request: HTTP request with no fields but token attached
    :return: list of all options serialised
    '''
    positions = Option.objects.all()
    serializer = OptionSerializer(positions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_option(request):
    '''
    :param request: HTTP request with 'position' fields
    :return: details of position
    '''

    data = {
        'trade_id': request.data.get('trade_id'),
        'symbol': request.data.get('symbol'),
        'strike': request.data.get('strike'),
        'expiration': date.today() + timedelta(request.data.get('dte')),
        'type': request.data.get('type'),
        'bought': request.data.get('bought'),
        'active': 1,
        'date_opened': date.today(),
    }
    position_serializer = OptionSerializer(data=data)
    if position_serializer.is_valid():
        position_serializer.create()
        return Response(position_serializer.data, status=status.HTTP_201_CREATED)

    return Response(position_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
