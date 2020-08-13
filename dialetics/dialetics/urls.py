from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/', include('topics.urls')),
    path('', include('home.urls')),
]
