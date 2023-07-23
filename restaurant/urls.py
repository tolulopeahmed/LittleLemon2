# urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    # ... Other URL patterns ...
    path('', views.index, name='index'),  # Add this line
    path('menu/', views.MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-retrieve-update-destroy'),
    path('api-auth/', include('rest_framework.urls')),  # Include this line

]
