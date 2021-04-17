from django.conf import settings
from celery import shared_task
from VideoSync.celery import app
import time

@app.task
def send_message(times):
    for i in range(times):
        print(f"Sending message {i} time")
        time.sleep(1.5)
        print(f"Sent message {i} time")