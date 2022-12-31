from django.shortcuts import render, redirect, reverse, get_object_or_404
from advertising.models import Advertise


def home(request):
    advertise = Advertise.objects.filter(status='p').order_by('-publish')
    return render(request, 'home/home.html', context={'ad': advertise})


def detail(request, id, slug):
    ad_detail = get_object_or_404(Advertise, id=id, slug=slug)
    return render(request, 'home/detail.html', context={'advertise': ad_detail})


def search_result(request):
    q = request.GET.get('q')
    ads = Advertise.objects.filter(title__icontains=q)
    return render(request, 'home/home.html', context={'ad': ads})
