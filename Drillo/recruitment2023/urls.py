from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.forms, name="forms"),
    path('submitted/', views.submit, name="submit")
]