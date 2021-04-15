from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#from rest_framework.routers import SimpleRouter



#router = SimpleRouter()

#API endpoints
#router.register('api/notes',NoteList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('api/', include('api.urls')),
]

#urlpatterns += router.urls

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
