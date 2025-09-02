from django.db import models

class Patient(models.Model):
    # Basic Information
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Medical Information
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    chronic_conditions = models.TextField(blank=True, null=True)  # e.g. Diabetes, Hypertension
    disease = models.TextField(blank=True, null=True)
    past_surgeries = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    vaccinations = models.TextField(blank=True, null=True)

    # Doctor / Hospital Info
    doctor_name = models.CharField(max_length=100, blank=True, null=True)
    doctor_contact = models.CharField(max_length=15, blank=True, null=True)
    hospital_name = models.CharField(max_length=150, blank=True, null=True)
    insurance_id = models.CharField(max_length=50, blank=True, null=True)

    # Reports (file uploads)
    report = models.FileField(upload_to="reports/", blank=True, null=True)

    # Emergency Info
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    emergency_notes = models.TextField(blank=True, null=True)

    # Meta Info
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name