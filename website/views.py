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
def search_projects(request):

    # search for a user by their username
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})

def projects(request):
    if request.GET.get('search_term'):
        projects = Project.search_project(request.GET.get('search_term'))
    else:
        projects = projects.all()
     form = NewsLetterForm

    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home_projects')

    return render(request, 'index.html', {'projects':projects, 'letterForm':form})
 