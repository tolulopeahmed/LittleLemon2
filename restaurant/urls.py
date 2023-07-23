# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... Other URL patterns ...
    path('', views.index, name='index'),  # Add this line
]
