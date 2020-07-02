from rest_framework import serializers
from .models import *

class BranchDetailsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchDetails
        fields = "__all__"

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

class BranchDetailsReadSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    class Meta:
        model = BranchDetails
        fields = "__all__"