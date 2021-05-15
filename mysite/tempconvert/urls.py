from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tempconvert/', include('tempconvert.urls')),
    path('admin/', admin.site.urls),
]