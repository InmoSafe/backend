from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create(request):
    return Response({"passed!"})

@api_view(['POST'])
def delete(request):
    return Response({"passed!"})

@api_view(['GET'])
def list(request):
    return Response({"passed!"})