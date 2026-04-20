from rest_framework import viewsets, filters, views
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        status = self.request.query_params.get('status')
        patient_id = self.request.query_params.get('patient')
        
        if status:
            queryset = queryset.filter(status=status)
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
            
        return queryset

    # GET /api/appointments/upcoming/
    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        upcoming_appointments = Appointment.objects.filter(
            date__gte=timezone.now(),
            status="Scheduled"
        ).order_by('date')
        
        serializer = self.get_serializer(upcoming_appointments, many=True)
        return Response(serializer.data)

class StatsView(views.APIView):
    def get(self, request):
        total_patients = Patient.objects.count()
        total_appointments = Appointment.objects.count()
        
        return Response({
            "total_patients": total_patients,
            "total_appointments": total_appointments
        })
