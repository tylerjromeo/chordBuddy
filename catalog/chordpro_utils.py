from chopro.core import ChoPro
import os
from .models import Song


def save_song_from_file(file_path):
    with open(file_path) as file:
        title, ext = os.path.splitext(os.path.basename(file_path))
        song = Song(title=title, chordpro_data=file.read())
        song.save()


def load_song_files(directory):
    from os import listdir
    from os.path import isfile, join
    songs = [f for f in listdir(directory) if isfile(join(directory, f))]
    list(map(lambda x:save_song_from_file(join(directory, x)), songs))


def get_html_from_chordpro_string(chordpro_string):
    chopro = ChoPro(chordpro_string)
    return chopro.get_html()

