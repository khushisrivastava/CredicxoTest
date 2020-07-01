from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BranchListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city']

class BranchViewSet(viewsets.ModelViewSet):
    queryset = BranchDetails.objects.all()
    serializer_class = BranchDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ifsc']
