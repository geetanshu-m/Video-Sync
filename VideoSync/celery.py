import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VideoSync.settings')

app = Celery('VideoSync')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {  
    'add-every-10-seconds': {
        'task': 'YoutubeApis.tasks.fetch_youtube_data',
        'schedule': 10,
    },
}