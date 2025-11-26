from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("nuevo/", views.crear_alumno, name="crear_alumno"),
    path("pdf/<int:alumno_id>/", views.enviar_pdf, name="enviar_pdf"),
]