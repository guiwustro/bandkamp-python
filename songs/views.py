from django.shortcuts import get_object_or_404
from rest_framework.views import Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
import ipdb

class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        album_id = self.kwargs["pk"]
        album = get_object_or_404(Album, id=album_id)
        serializer.save(album=album)
        