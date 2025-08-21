from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from marcenaria_app import views  # <-- isso aqui é importante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marcenaria_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
