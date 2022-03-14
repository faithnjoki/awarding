from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=300)
    contact = models.CharField(max_length=100)

    def save_profile(self):
        self.save()
    
    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    image = CloudinaryField("image")
    url = models.URLField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def search_project_name(cls, search_term):
        projects = cls.objects.filter(
        title__icontains=search_term)
        return projects 

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.IntegerField(default=0, blank=True, null=True)
    usability_rate = models.IntegerField(default=0, blank=True, null=True)
    content_rate = models.IntegerField(default=0, blank=True, null=True)
    avarage_rate = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.project