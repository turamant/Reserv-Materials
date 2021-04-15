from django.urls import path
from .views import NoteList, NoteDetail

urlpatterns = [
    path('<int:pk>/', NoteDetail.as_view()),
    path('', NoteList.as_view()),
]