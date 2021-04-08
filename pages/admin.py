from django.contrib import admin

# Register your models here.
from pages.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name','slug','image')
    prepopulated_fields = {"slug":('name',),}
