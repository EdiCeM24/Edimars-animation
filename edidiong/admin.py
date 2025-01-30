from django.contrib import admin # type: ignore
from . models import About, AboutVideo, VideoProject, Project, Home, Blog, BlogVideo



class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'created_at')
    
    
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_display', 'text', 'created_at')
    
    
class AboutVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_image', 'text', 'created_at')
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'text', 'created_at')
    
    
class BlogVideoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'video', 'description', 'created_at')
    
        
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'created_at')
    

class VideoProjectAdmin(admin.ModelAdmin):
    list_display = ('caption', 'video', 'description')
    
    
    
    
    
admin.site.register(Home, HomeAdmin)
    
admin.site.register(About, AboutAdmin)

admin.site.register(AboutVideo, AboutVideoAdmin)

admin.site.register(Blog, BlogAdmin)

admin.site.register(BlogVideo, BlogVideoAdmin) 
   
admin.site.register(Project, ProjectAdmin)    

admin.site.register(VideoProject, VideoProjectAdmin)    
