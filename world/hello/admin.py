from django.contrib import admin # type: ignore
from .models import KYC

@admin.register(KYC)
class KYCAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'gender', 'email')
