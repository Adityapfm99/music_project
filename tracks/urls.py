from django.urls import path
from .views import TrackUploadView,TrackListAPIView, TrackDetailAPIView, TrackDeleteAPIView, TrackUpdateAPIView

urlpatterns = [
    path('api/tracks/', TrackUploadView.as_view(), name='track-upload'),
    path('api/tracks/list', TrackListAPIView.as_view(), name='track-list'),
    path('api/tracks/detail/<int:pk>', TrackDetailAPIView.as_view(), name='track-detail'),
    path('api/tracks/update/<int:pk>', TrackUpdateAPIView.as_view(), name='track-update'),
    path('api/tracks/delete/<int:pk>', TrackDeleteAPIView.as_view(), name='track-delete'),
]
