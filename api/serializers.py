from rest_framework import serializers

from pages.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id','name','family','slug','text',
                  'image','price','quantity','computing_price','nalog_nds')