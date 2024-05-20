from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from rest_framework import permissions
from .views import TrackUploadView,TrackListAPIView, TrackDetailAPIView, TrackDeleteAPIView, TrackUpdateAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Music Project API",
        default_version='v1',
        description="API documentation for the Music Project App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/tracks/', TrackUploadView.as_view(), name='track-upload'),
    path('api/tracks/list', TrackListAPIView.as_view(), name='track-list'),
    path('api/tracks/detail/<int:pk>', TrackDetailAPIView.as_view(), name='track-detail'),
    path('api/tracks/update/<int:pk>', TrackUpdateAPIView.as_view(), name='track-update'),
    path('api/tracks/delete/<int:pk>', TrackDeleteAPIView.as_view(), name='track-delete'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)