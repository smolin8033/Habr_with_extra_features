from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api/', include('djoser.urls')),
    # url(r'^api/', include('posts.urls')),
    url(r'^api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
