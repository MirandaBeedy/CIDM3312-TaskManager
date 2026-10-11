
from django.shortcuts import render

tasks = [
    {"title": "Buy groceries", "done": True},
    {"title": "Finish CIDM 3312 homework", "done": False},
    {"title": "Email the study group", "done": False},
    {"title": "Renew library books", "done": True},
    {"title": "Prepare project proposal", "done": False},
    {"title": "Walk the dogs", "done": False},
]


def home(request):
    return render(request, "home.html", {"tasks": tasks})


def about(request):
    return render(request, "about.html")

