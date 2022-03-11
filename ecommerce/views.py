from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def checkServer(request):
    date = datetime.now().strftime(" %d/%m/%Y %H:%M:%S")
    message = 'server is running'
    return Response(data=message + date ,status = status.HTTP_200_OK )
