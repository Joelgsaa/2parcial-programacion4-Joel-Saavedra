from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Alumno
from .forms import AlumnoForm
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from io import BytesIO

@login_required
def dashboard(request):
    alumnos = Alumno.objects.filter(usuario=request.user)
    return render(request, "alumnos/dashboard.html", {"alumnos": alumnos})

@login_required
def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.usuario = request.user
            alumno.save()
            return redirect("dashboard")
    else:
        form = AlumnoForm()
    return render(request, "alumnos/alumno_form.html", {"form": form})

@login_required
def enviar_pdf(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id, usuario=request.user)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Alumno: {alumno.nombre}")
    p.drawString(100, 730, f"Edad: {alumno.edad}")
    p.drawString(100, 710, f"Carrera: {alumno.carrera}")
    p.showPage()
    p.save()
    buffer.seek(0)

    email = EmailMessage("Datos Alumno",
    "Adjunto PDF",
    to=["ematevez@gmail.com"])
    email.attach("alumno.pdf", buffer.read(), "application/pdf")
    email.send()
    return redirect("dashboard")