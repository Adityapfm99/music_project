from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Track
from .serializers import TrackSerializer

class TrackUploadView(APIView):
   def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        artist = request.data.get('artist')
        title = request.data.get('title')
        if file_obj is not None:
            track = Track.objects.create(file=file_obj, artist=artist, title=title)
            serializer = TrackSerializer(track)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
class TrackDetailAPIView(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
        
class TrackListAPIView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = () 
    
class TrackDeleteAPIView(generics.DestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = ()

    def delete(self, request, *args, **kwargs):
        data = self.get_object()
        if data:    
            data.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)

       