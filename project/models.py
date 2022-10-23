from django.db import models

# Create your models here.

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    

class Design(models.Model):
    image = models.FileField(upload_to='designs/')

class Feedback(models.Model):
    feedback = models.TextField(max_length=1024, default="NA")
    image = models.FileField(upload_to='feedbacks/')
    video = models.FileField(upload_to="feedbacks/vid", default="NA")
    user_name = models.CharField(max_length=100, default="Client")
    project_name = models.CharField(max_length=100, default="Project")

class Project(models.Model):
    name = models.CharField(max_length=100, null=False, default="Modular Kitchen")
    tagline = models.CharField(max_length=300, default="NA")
    description = models.TextField(max_length=1000, default="NA")
    project_img = models.FileField(upload_to='projects/')
    design_complete = models.BooleanField(default=False)
    building_complete = models.BooleanField(default=False)
    full_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class PostImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    site = models.CharField(max_length=100, default="Site 1")
    date = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to = 'images/progress/')

    def __str__(self):
        return self.project.name