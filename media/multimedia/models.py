from django.db import models

# Create your models here.
class ImageMedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.name


class AudioMedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/audio/')

    def __str__(self):
        return self.name


class VideoMedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/video/')

    def __str__(self):
        return self.name