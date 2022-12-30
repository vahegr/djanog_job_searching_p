from django.shortcuts import render
from .models import About


def about(request):
    about_us = About.objects.get(status=True, id=1)
    return render(request, 'about/about.html', context={'about': about_us})
