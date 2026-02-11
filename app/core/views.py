from django.shortcuts import render


def index(request):
    """Landing page showing authentication status."""
    return render(request, "core/index.html")
