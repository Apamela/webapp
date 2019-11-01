# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from .models import  Image, Review,Profile
from django.core.files.uploadedfile import SimpleUploadedFile


#************************************Testing instance****************************************************************8

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):


        self.test_image = Image.objects.create(image='babyjp',name='gu',description='This is a description')
                                
        self.test_image.save()

    def test_save_method(self):
        self.test_image.save()
        test_images = Image.objects.all()
        self.assertTrue(len(test_images) > 0)

 Testing save method
    def test_save_image(self):
        self.assertEqual(len(Image.objects.all()), 1)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Tear down method*********************************************************************888******888******8888888888************8888888
    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        Image.delete_image_by_id(self.test_image.id)
        self.assertEqual(len(Image.objects.all()), 0)



class Review(TestCase):

    def setUp(self):

       
        self.picture = Image.objects.create(image='babyjp',
                                            
        self.comment = Review.objects.create(comment = 'happines')

        self.test_review = Review.objects.create(user=self.lol,
                                                 image=self.picture,
                                                 comment='happinesphoto')
        self.test_review.save()

    #********************************************88Testing instance*************************************************88***********************************8*********************8888888*88

    def test_instance(self):

        self.assertTrue(isinstance(self.test_reviews, Review))

    #***************************************************************88Testing Save method*********************************************************************************************88

    def test_save_method(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_save_review(self):
        self.assertEqual(len(Review.objects.all()), 1)

    #********************************************************************88 Tear down method******************************************************8****************8*88********88888******
    def tearDown(self):
        Review.objects.all().delete()

  #******************************************************************8 Testing delete method**********************************************************************8***********88888888888***

    def test_delete_review(self):
        self.test_review.delete()
        self.assertEqual(len(Review.objects.all()), 0)
