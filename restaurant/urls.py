# urls.py

from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from . import views
from .views import protected_view

urlpatterns = [
    # ... Other URL patterns ...
    path('', views.index, name='index'),  # Add this line
    path('protected/', views.protected_view, name='protected-view'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-retrieve-update-destroy'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls')),  # Include this line
    path('api-token-auth/', obtain_auth_token),
    path('api/protected/', protected_view, name='protected-view'),
]
