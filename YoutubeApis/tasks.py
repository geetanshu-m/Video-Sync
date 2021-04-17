from VideoSync.celery import app
from .utils import YoutubeDataFetch
from VideoSync.settings import env

@app.task
def fetch_youtube_data():
    q = env('QUERY')
    YoutubeDataFetch(q)