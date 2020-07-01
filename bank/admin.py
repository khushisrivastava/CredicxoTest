from django.contrib import admin
from .models import *

class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_id', 'name', 'city', 'state', )

admin.site.register(Bank, BankAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('bank', 'branch', 'ifsc', 'address', 'district')


admin.site.register(BranchDetails, BranchAdmin)