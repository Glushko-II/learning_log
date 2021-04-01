from django.shortcuts import render


def index(request):
    """Доиашняя страница приложения Learning Log"""
    return render(request, "learning_logs/index.html")
