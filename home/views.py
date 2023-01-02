from django.shortcuts import render, redirect, reverse, get_object_or_404
from advertising.models import Advertise
from advertising.forms import AddAdvertiseForm, EditResumeForm
from account.models import User
from chat.models import Room


def home(request):
    advertise = Advertise.objects.filter(status='p').order_by('-publish')
    resumes = User.objects.filter(type_of_user='1')
    return render(request, 'home/home.html', context={'ad': advertise, 'resumes': resumes})


def detail(request, id, slug):
    ad_detail = get_object_or_404(Advertise, id=id, slug=slug)
    return render(request, 'home/detail.html', context={'advertise': ad_detail})


def search_result(request):
    q = request.GET.get('q')
    ads = Advertise.objects.filter(title__icontains=q, status='p').order_by('-publish')
    resumes = User.objects.filter(skill__icontains=q, type_of_user='1')
    return render(request, 'home/home.html', context={'ad': ads, 'resumes': resumes})


def my_advertises(request):
    ads = Advertise.objects.filter(user_id=request.user.id, status='p').order_by('-publish')
    return render(request, 'home/home.html', context={'ad': ads})


def add_advertise(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = AddAdvertiseForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('home:my advertises')
        else:
            form = AddAdvertiseForm()
        return render(request, 'home/advertise.html', context={'form': form})
    else:
        return redirect('home:home')


def edit_resume(request, username):
    the_user = User.objects.get(username=username)
    user = request.user
    if the_user.type_of_user == '1' and user.is_authenticated:
        if the_user.username == user.username:
            form = EditResumeForm(instance=user)
            if request.method == 'POST':
                form = EditResumeForm(instance=user, data=request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('home:home')
            return render(request, "home/Resume.html", context={'form': form, 'the_user': the_user})
        else:
            return redirect('home:home')
    else:
        return redirect('home:home')


def resume_detail(request, user_id):
    user_resume = User.objects.get(id=user_id, type_of_user='1')
    return render(request, 'home/Resumedetail.html', context={'user_resume': user_resume})
