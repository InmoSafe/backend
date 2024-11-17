from rest_framework import generics
from inmuebles_app.models import Inmueble
from inmuebles_app.api.serializers import InmuebleSerializer

class ApCreate(generics.CreateAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class ApUpdate(generics.UpdateAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class ApDelete(generics.DestroyAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class ApList(generics.ListAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class ApDetail(generics.RetrieveAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer