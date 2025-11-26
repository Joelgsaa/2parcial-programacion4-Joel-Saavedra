import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.core.mail import send_mail

def scraper_view(request):
    results = []
    if request.method == "POST":
        keyword = request.POST.get("keyword")
        url = f"https://es.wikipedia.org/wiki/{keyword}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = [p.text for p in soup.select("p")[:5]]

        send_mail(
            "Resultados Scraper",
            "\n".join(results),
            "noreply@tuapp.com",
            [request.user.email],
        )
    return render(request, "scraper/scraper.html", {"results": results})