from django.shortcuts import render
from catalog.models import Test
from catalog.serializers import TestSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {obj['timestamp']: obj['uuid'] for obj in serializer.data}
        return Response(data)