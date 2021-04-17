from .models import YoutubeVideos
from rest_framework import serializers

class YoutubeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideos
        fields = [
            'video_id',
            'title',
            'description',
            'publish_time',
            'thumbnails',
            'video_url'
        ]
        read_only_fields = ['video_url']