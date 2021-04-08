from django.urls import path
from pages.views import NoteDetailView, NoteListView,HomeView, sea

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('sea/', sea, name='sea'),
    path('notes/',NoteListView.as_view(), name='list'),
    path('notes/<slug:slug>/',NoteDetailView.as_view(), name='detail'),


]