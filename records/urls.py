from django.conf.urls.static import static
from django.conf import settings
from records.views import index, records, id
from django.urls import path

app_name = 'record'

urlpatterns = [
    path('', records, name='records'),
    path('<id>', id, name='id')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)