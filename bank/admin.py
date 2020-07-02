from django.contrib import admin
from .models import *

class BankAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Bank, BankAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('bank', 'branch', 'ifsc', 'address', 'district', 'city', 'state',)


admin.site.register(BranchDetails, BranchAdmin)