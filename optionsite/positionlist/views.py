from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Option
from .serializers import OptionSerializer
from rest_framework import status


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
