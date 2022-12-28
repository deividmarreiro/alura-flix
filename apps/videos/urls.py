from django.urls import path
from . import api

urlpatterns = [
    path('videos/', api.VideoListView.as_view(), name='video-list'),
    path('videos/<int:pk>/', api.VideoDetailView.as_view(), name='video-detail'),
    path('videos/create/', api.VideoCreateView.as_view(), name='video-create'),
    path('videos/<int:pk>/update/', api.VideoUpdateView.as_view(), name='video-update'),
    path('videos/<int:pk>/delete/', api.VideoDeleteView.as_view(), name='video-delete'),
]
