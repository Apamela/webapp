# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime as dt
# Create your models here.
#...................................class for Profile.......................................
class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    date = models.DateTimeField(auto_now_add=True, null= True)
    class Meta:
        db_table = 'profile'
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_users(cls,search_iterm):
        profiles = cls.objects.filter(user__username__icontains =search_term)
        return profiles
    def __str__(self):
        return self.user
#.........................................class for project..................................
class Project(models.Model):
    title = models.TextField(max_length=100,null=True,blank=True,default="title")
    description = models.TextField()
    project_image = models.ImageField(upload_to='picture/',null=True,blank=True)
    def save_project(self):
        self.save()
    @classmethod
    def delete_project_by_id(cls,id):
        projects = cls.objects.filter(pk=id)  
        projects.delete()  
    @classmethod
    def get_project_by_id(cls,id):
        projects = cls.objects.get(pk= id)
        return projects
    @classmethod
    def search_projects(cls,search_term):
        projects = cls.objects.filter(title_icontains=search_term)
        return projects