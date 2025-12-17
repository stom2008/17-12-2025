from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def quiz_page(request):
    return render(request, "quiz-page.html")

def result(request):
    return render(request, "result.html")
