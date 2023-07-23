# urls.py (project level)
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'booking/tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu-list-create'),
    path('api/protected/', views.protected_view, name='protected-view'),  # Move this line above 'api/' URL pattern
    path('api/', include(router.urls)),  # Move the API URLs below other specific URLs
    path('restaurant/', include('restaurant.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
