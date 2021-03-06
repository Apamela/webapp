# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
import datetime as dt
# Create your models here.
#...................................class for Profile.......................................
class Profile (models.Model):
    user = user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
    bio = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    date = models.DateTimeField(auto_now_add=True, null= True)
    class Meta:
        db_table = 'profile'
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)
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
#.........................................class for project..................................................
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
#...................................................class for Image............................................
class Image(models.Model):
    image=models.ImageField(upload_to='picture/', )
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="images")
    description=models.TextField()
    likes = models.IntegerField(default=0)
    comments= models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
    @classmethod
    def delete_image_by_id(cls,id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    @classmethod
    def search_image(cls,search_term):
        pictures = cls.objects.filter(name_icontains=search_term)
        return pictures

    @classmethod
    def update_image(cls,id):
       pictures=cls.objects.filter(id=id).update(id=id)
       return pictures
#........................................................class for review.............................................
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

    )
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)

    def save_comment(self):
        self.save()

    def get_comment(self, id):
        comments = Review.objects.filter(image_id =id)
        return comments

    def __str__(self):
        return self.comment
#****************************************** class on NewsLetterRecipients ***************************************************************************
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
