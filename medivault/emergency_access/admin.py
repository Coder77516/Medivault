from django.contrib import admin
from .models import Patient
 
class PatientAdmin(admin.ModelAdmin):
     list_display = ("id", "name", "age", "blood_group", "phone")
     search_fields = ("name", "phone")

