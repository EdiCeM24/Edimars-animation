from django.contrib import admin # type: ignore
from . models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'video', 'description')
    
    
    
    
    
admin.site.register(Video, VideoAdmin)    
