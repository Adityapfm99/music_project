import mimetypes
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import librosa
from .models import Track
from .serializers import TrackSerializer

class TrackUploadView(APIView):
   def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        artist = request.data.get('artist')
        title = request.data.get('title')
        if file_obj is None:
            return Response({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check file extension only allow mp3
        if not file_obj.name.lower().endswith('.mp3'):
            return Response({'error': 'Only MP3 files are allowed'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check MIME type
        mime_type, _ = mimetypes.guess_type(file_obj.name)
        if mime_type != 'audio/mpeg':
            return Response({'error': 'Invalid file type. Only MP3 files are allowed'}, status=status.HTTP_400_BAD_REQUEST)
        
        track = Track.objects.create(file=file_obj, artist=artist, title=title)
        serializer = TrackSerializer(track)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
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


class CalculateStartTimeAPIView(generics.GenericAPIView):
    queryset = Track.objects.all()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        track = get_object_or_404(Track, pk=kwargs['pk'])
        file_path = track.file.path
        
        y, sr = librosa.load(file_path, sr=None)
        start_time = librosa.effects.split(y, top_db=20)[0][0] / sr
        
        return Response({"start_time": start_time}, status=status.HTTP_200_OK)