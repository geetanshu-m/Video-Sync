import requests
from django.db.models import Max
from .models import YoutubeVideos
from .serializers import YoutubeVideosSerializer
from datetime import datetime, timedelta
from VideoSync.settings import env

class YoutubeDataFetch():
    api_key = env('YOUTUBE_API_KEY')
    url = "https://www.googleapis.com/youtube/v3/search"
    keys = ['title', 'description', 'publishTime', 'thumbnails']
    
    def __init__(self, q):
        self.q = q
        self.process_seq()

    def get_latest_video_time(self):
        self.publisedAfter = YoutubeVideos.objects.aggregate(Max('publish_time'))['publish_time__max']
        if self.publisedAfter is None:
            time_after = datetime.now() - timedelta(minutes=30)
            self.publisedAfter = time_after.isoformat()[:-4]+'Z'
        else:
            self.publisedAfter = self.publisedAfter.isoformat()[:-6]+'Z'

    
    def fetch_data(self):
        params = {
            'key':self.api_key,
            'type':'video', 
            'order':'date', 
            'q':self.q,
            'maxResults':50,
            'part':'snippet',
            'publishedAfter': self.publisedAfter
        }
        self.data = requests.get(self.url,params=params).json()
        
    def clean_data(self):
        self.cleaned_data = []
        for vr in self.data['items']:
            o = {
                'video_id':vr['id']['videoId'],
                'title':vr['snippet']['title'],
                'description':vr['snippet']['description'],
                'publish_time':vr['snippet']['publishTime'],
                'thumbnails':vr['snippet']['thumbnails']
            }
            self.cleaned_data.append(o)
    
    def save_to_db(self):
        # Filtering the Videos that are not present in the db
        video_ids = list(map(lambda x: x['video_id'], self.cleaned_data))
        ids_present = YoutubeVideos.objects.all().filter(pk__in=video_ids).values('video_id')
        ids_present = list(map(lambda x: x['video_id'], ids_present))
        self.cleaned_data = list(filter(lambda x : x['video_id'] not in ids_present, self.cleaned_data))
        print(f"Out of {len(video_ids)}, {len(ids_present)} was already there, inserting remaining {len(self.cleaned_data)}")
        
        serialized_data = YoutubeVideosSerializer(data=self.cleaned_data, many=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()

    def process_seq(self):
        print("Starting Youtube Fetch")
        self.get_latest_video_time()
        print(f"Getting Videos after {self.publisedAfter}")
        self.fetch_data()
        print("Got the data for youtube API's")
        print("Cleaning data now")
        self.clean_data()
        print(f"Data Cleaned, total {len(self.cleaned_data)} objects")
        print("Now pushing the clean data in database")
        self.save_to_db()
        print("Data successfully saved in DB")
        print("Exiting the Sequence")