from django.urls import path
from . import views
from .views import SongListView

urlpatterns = [
    path('', views.home, name='catalog-home'),
    path('songs/', SongListView.as_view(), name='song-list'),
    path('songs/<int:song_id>/', views.song_details, name='song-detail'),
]
