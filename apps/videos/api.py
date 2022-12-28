from rest_framework import generics
from .serializers import VideoSerializer
from .models import Video

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class VideoDetailView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class VideoCreateView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class VideoUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
    
class VideoDeleteView(generics.DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer