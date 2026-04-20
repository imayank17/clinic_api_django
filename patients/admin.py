from django.contrib import admin
from .models import Patient, Appointment

class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "phone")
    search_fields = ("name",)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor_name", "date")
    list_filter = ("doctor_name",)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
