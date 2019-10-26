# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime as dt
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('profile')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})
def projects(request):
    if request.GET.get('search_term'):
        projects = Project.search_project(request.GET.get('search_term'))
    else:
        projects = projects.all()
    form = 