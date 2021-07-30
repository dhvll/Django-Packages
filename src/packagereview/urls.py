from django.contrib import admin
from django.urls import path, include
from .views import UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('me/', UserDetailView.as_view())
]
