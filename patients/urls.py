from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AppointmentViewSet, StatsView

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('stats/', StatsView.as_view(), name='stats'),
    path('', include(router.urls)),
]
