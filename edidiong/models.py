from django.db import models # type: ignore

from embed_video.fields import EmbedVideoField # type: ignore



class Video(models.Model):
    caption = models.CharField(max_length=255)
    video = models.URLField()
    description = models.TextField()


    def __str__(self):
        return self
