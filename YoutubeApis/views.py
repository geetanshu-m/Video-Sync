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

        # Filtering the Videos that are not present in the db
        video_ids = list(map(lambda x: x['video_id'], data))
        ids_present = YoutubeVideos.objects.all().filter(pk__in=video_ids).values('video_id')
        ids_present = list(map(lambda x: x['video_id'], ids_present))
        data_to_insert = list(filter(lambda x : x['video_id'] not in ids_present, data))
        serialized_data = self.serializer_class(data=data_to_insert, many=True)
        
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response({
            "Message" : f"{len(data)} Created",
            'video_ids':video_ids,
            'ids_p':ids_present,
            'data_to_insert':data_to_insert
        })