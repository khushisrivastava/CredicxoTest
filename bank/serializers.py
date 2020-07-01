from rest_framework import serializers
from .models import *

class BranchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchDetails
        fields = "__all__"
        read_only_fields = ['bank_details', 'branch', 'address', 'district']

class BranchListSerializer(serializers.ModelSerializer):
    branch = serializers.SerializerMethodField()
    class Meta:
        model = Bank
        fields = ['name', 'city', 'branch']

    def get_branch(self, obj):
        branch = BranchDetails.objects.filter(bank=obj)
        branch_serializer = BranchDetailsSerializer(branch, many=True)
        return branch_serializer.data
