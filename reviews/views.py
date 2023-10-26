from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def welcome_view(request):
    return render(request, "base.html")


def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})


def search_result(request):
    search_words = request.GET.get("search") or ""
    return render(request, "search_result.html", {"search_words": search_words})
