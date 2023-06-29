from django.urls import path
from .views import *

urlpatterns = [
    path('create', form_submission, name='form_submission'),
    path('MyDynamicModel', MyDynamicModel, name='create'),
    path('<slug:url>/', page_preview, name='page_preview'),
]