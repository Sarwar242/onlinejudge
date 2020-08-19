from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    #path('', include('Judge.urls')),
    path('admin/', admin.site.urls),
    path('api/profile/',include('Profile.urls')),
    path('api/auth/jwt/', obtain_jwt_token),
    path('api/auth/jwt/refresh/', refresh_jwt_token),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
