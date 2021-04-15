from django.contrib import admin

# Register your models here.
from pages.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name','family','slug',
                    'image','price','quantity',
                    'computing_price','nalog_nds')
    prepopulated_fields = {"slug":('name',),}
