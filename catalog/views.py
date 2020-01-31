from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Song

# Create your views here.


def home(request):
    context = {
        'title': 'home'
    }
    return render(request, 'catalog/home.html', context)


def song_details(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    context = {
        'title': song.title,
        'song_html': '<h2>Song goes here</h2>'
    }
    return render(request, 'catalog/song_detail.html', context)


class SongListView(ListView):
    model = Song
