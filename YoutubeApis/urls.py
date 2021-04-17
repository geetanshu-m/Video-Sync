from django.urls import path
from rest_framework import routers
from .views import YoutubeVideosViewSet

router = routers.SimpleRouter()
router.register(r"", YoutubeVideosViewSet)

urlpatterns = router.urls