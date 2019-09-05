from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('', include('blog.urls')),
    path('eventos/', include('eventos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
