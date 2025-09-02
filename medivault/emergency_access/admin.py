from django.contrib import admin
from .models import Patient

# @admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "gender", "blood_group", "phone", "updated_at")
    search_fields = ("name", "phone", "email", "blood_group")
    list_filter = ("gender", "blood_group", "updated_at")

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "age", "gender", "phone", "email", "address")
        }),
        ("Medical Information", {
            "fields": (
                "blood_group", "allergies", "chronic_conditions",
                "disease", "past_surgeries", "medical_history",
                "current_medications", "vaccinations"
            )
        }),
        ("Doctor / Hospital Info", {
            "fields": ("doctor_name", "doctor_contact", "hospital_name", "insurance_id")
        }),
        ("Reports", {
            "fields": ("report",)
        }),
        ("Emergency Info", {
            "fields": ("emergency_contact", "emergency_notes")
        }),
        ("Meta Info", {
            "fields": ("updated_at",),
            "classes": ("collapse",),  # collapsible section
        }),
    )

    readonly_fields = ("updated_at",)

