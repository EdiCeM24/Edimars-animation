from django.db import models # type: ignore

from embed_video.fields import EmbedVideoField # type: ignore



class Home(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    description = models.TextField()
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    
class About(models.Model):
    name = models.CharField(max_length=100)
    image_display = models.ImageField(upload_to='foler/wame')
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
    
    
class AboutVideo(models.Model):
    title = models.CharField(max_length=255)
    video_image = models.FileField(upload_to='video_store', blank=True, null=True)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='app-board', blank=True, null=True)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class BlogVideo(models.Model):
    caption = models.CharField(max_length=255)
    video = models.FileField(upload_to='media/view')
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    

class Project(models.Model):
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='stores', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)   
     
    def __str__(self):
        return self.description   
    
        
class VideoProject(models.Model):
    caption = models.CharField(max_length=255)
    video = models.FileField(upload_to='appstore')
    description = models.TextField()


    def __str__(self):
        return self.caption
