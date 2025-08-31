from django.urls import path
from . import views

urlpatterns = [
    path("generate_qr/<int:patient_id>/", views.generate_qr, name="generate_qr"),
    path("patient/<int:patient_id>/", views.patient_detail, name="patient_detail"),
]