from pages.models import Note
from api.serializers import NoteSerializer
from rest_framework import generics

class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    #permission_classes = (permissions.IsAuthenticated,)

class NoteDetail(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer