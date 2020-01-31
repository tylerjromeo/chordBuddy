from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Song(models.Model):
    title = models.CharField(max_length=256)
    chordpro_data = models.TextField()
    tags = models.ManyToManyField(Tag)


class Link(models.Model):
    class LinkType(models.TextChoices):
        YOUTUBE = 'YOUTUBE'
        WEB_PAGE = 'WEB_PAGE'

    url = models.CharField(max_length=256)
    type = models.CharField(max_length=16, choices=LinkType.choices)
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
