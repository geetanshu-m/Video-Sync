from django.db import models

# Create your models here.
class YoutubeVideos(models.Model):
    class Meta:
        db_table = "youtube_videos"

    video_id = models.CharField(max_length=15, primary_key=True)
    title = models.TextField()
    description = models.TextField()
    publish_time = models.DateTimeField()
    thumbnails = models.JSONField()

    @property
    def video_url(self):
        return f"https://www.youtube.com/watch?v={self.video_id}"

    