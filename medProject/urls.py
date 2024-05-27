from django.contrib import admin
from django.urls import path, include
from employee.views import profile
from records.views import index, records
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('employee/', include('employee.urls', namespace='employee')),
    path('records/', include('records.urls', namespace='record'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
