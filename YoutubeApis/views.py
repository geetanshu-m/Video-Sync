from rest_framework import viewsets
from .models import YoutubeVideos
from rest_framework.response import Response
from .serializers import YoutubeVideosSerializer
# Create your views here.

class YoutubeVideosViewSet(viewsets.ModelViewSet):
    queryset = YoutubeVideos.objects.all().order_by('-publish_time')
    serializer_class = YoutubeVideosSerializer

    def create(self, request):
        data = request.data
        serialized_data = self.serializer_class(data=data, many=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response({
            "Message" : f"{len(data)} Created",
        })