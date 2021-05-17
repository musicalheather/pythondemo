from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tempconvert/', include('tempconvert.urls')),
    path('admin/', admin.site.urls),
]
