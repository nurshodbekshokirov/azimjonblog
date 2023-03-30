
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('blog/', blog),
    path('about/', about),
    path('maqola/<int:son>', maqola),
    path('interyu/', interyu),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
