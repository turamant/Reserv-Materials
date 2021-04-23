from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from pages.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name','family','slug',
                    "get_image",'price','quantity',
                    'computing_price','nalog_nds','computing_price')
    readonly_fields = ("get_image",)
    prepopulated_fields = {"slug":('name',),}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"
