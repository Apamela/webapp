# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm,NewProjectForm
from .forms import ReviewForm,UpdatebioForm
import datetime as dt

from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Project,Review,Image,NewsLetterRecipients

# Create your views here
#*********************************** the welcome page here***********************************************************************

def welcome(request):
    return render(request, 'welcome.html')
#************************************the pages for editing the images******************************************************************************************************************************************************************************************************************************************************

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES, instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = UpdatebioForm()
    return render(request, 'edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request, username=None):
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)

    return render (request, 'profile.html', {'images':images, 'username': username})
@login_required(login_url='/accounts/login/')
def profile_page(request, username):
    print(username)
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)
    user = request.user
    profile = Profile.objects.get(user=user)
    userf = User.objects.get(pk=username)
    latest_review_list = Review.objects.filter(user_id=username).filter(user_id=username)
    context = {'latest_review_list': latest_review_list}
    if userf:
        print('user found')
        profile = Profile.objects.get(user=userf)
    else:
        print('No suchuser')
    return render (request, '.html', context, {'images':images,'profile':profile,'user':user,'username': username})
                                                                
@login_required(login_url='/accounts/login/')
def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = NewImageForm()
    return render(request, 'image2.html', {"form": form})

#**************************************************the home pages of the project*************************************88
@login_required(login_url='/accounts/login/')
def home_projects(request):
    if request.GET.get('search_term'):
        projects = Project.search_project(request.GET.get('search_term'))

    else:
        projects = Project.objects.all()

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

    return render(request, 'welcome.html', {'projects':projects, 'letterForm':form})
#**********************************************************function for theproject.**************************************************************
def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()
    return render(request, 'image.html', {"project": project, 'form':form,'comments':comments, 'latest_review_list':latest_review_list})
                                                                             
#**8*8************************************nav bar for searching the project***************************
def search_projects(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})
def project_list(request):
     project_list= Project.objects.order_by('-title')
     contex = {'project_list':project_list}
     return render(request,'project_list.html',context)

def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('homePage')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

#******************************************************************Page for newsrecipients*************************************************
@login_required(login_url='/accounts/login/')
def newsletter(request):
    name = request.POST.get('your_name')
    email= request.POST.get('email')

    recipient= NewsLetterRecipients(name= name, email =email)
    recipient.save()
    send_welcome_email(name, email)
    data= {'success': 'You have been successfully added to the newsletter mailing list'}
    return JsonResponse(data)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})
def user(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'user.html', context)
