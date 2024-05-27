from django.conf.urls.static import static
from django.conf import settings
from employee.views import profile, logout, user
from django.urls import path

app_name = 'employee'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('<id>', user, name='user'),
    path('logout/', logout, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)