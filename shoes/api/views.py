from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Shoes, Sex, Brand
from .serializers import ShoesSerializer

class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

    @action(methods=['get'], detail=True)
    def get_sex(self, request, pk=None):
        sex = Sex.objects.get(pk=pk)
        return Response({'sex': sex.name})

    @action(methods=['get'], detail=True)
    def get_brand(self, request, pk=None):
        brand = Brand.objects.get(pk=pk)
        return Response({'brand': brand.name})
