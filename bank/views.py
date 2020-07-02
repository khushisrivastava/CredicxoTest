from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


class BranchViewSet(viewsets.ModelViewSet):
    queryset = BranchDetails.objects.all()
    # serializer_class = BranchDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ifsc', 'bank__name', 'city']

    def get_serializer_class(self):
        method = self.request.method
        if method == 'GET':
            return BranchDetailsReadSerializer
        else:
            return BranchDetailsWriteSerializer
