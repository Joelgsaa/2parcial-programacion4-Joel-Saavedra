from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                "Bienvenido",
                "Gracias por registrarte!",
                "noreply@tuapp.com",
                [user.email],
            )
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})