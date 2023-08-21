from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('eventman.urls')),
    path('user/', include('user.urls')),
    path('', views.home, name='home'),
]
