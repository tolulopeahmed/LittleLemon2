from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'booking/tables', views.BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Move the API URLs above 'restaurant/' URL
    path('restaurant/', include('restaurant.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
