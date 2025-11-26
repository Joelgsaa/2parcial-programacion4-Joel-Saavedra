# alumnos/forms.py
from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["nombre", "edad", "carrera"]