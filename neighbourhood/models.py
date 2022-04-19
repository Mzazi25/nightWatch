from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class NeighbourHood(models.Model):
    hood_name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="neighbourhood", null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.hood_name

    def save_neighbourhood(self):
        self.save_neighbourhood()

    def delete_neighbourhood(self):
        self.delete_neighbourhood()
    @classmethod
    def search_neighbourhood(cls, neighbourhood_id):
        neighbourhood = cls.objects.filter(id=neighbourhood_id)
        return neighbourhood


class Profile(models.Model):
    username = models.CharField(max_length =30)
    description = models.TextField(null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name="posts")
    neighbor_hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name="nighthood", null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
       return self.description 
    
    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length=150, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="business", null  =True, default='')
    neighbor_hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name="hooddy", null=True, default='')
    email = models.CharField(max_length=80, null=True, default='mzazi@ymal.com')

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, business_id):
        business = cls.objects.filter(id=business_id)
        return business

class Post(models.Model):
    image = CloudinaryField('image',blank=True)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='author')
    def __str__(self):
        return self.description

class Comments(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    comments = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    