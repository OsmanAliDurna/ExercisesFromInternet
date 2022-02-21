from django.shortcuts import render
from .forms import ContactForm

def home(request):
    form = ContactForm()
    context = {
        "form": form
    }
    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")


def teacher(request):
    return render(request, "home/teacher.html")