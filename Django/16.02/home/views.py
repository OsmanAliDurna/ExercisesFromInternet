from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")


def teacher(request):
    return render(request, "home/teacher.html")