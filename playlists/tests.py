from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from netflix.db.models import PublishStateOptions
from videos.models import Video
from .models import Playlist
# Create your tests here.

class VideoModelTestCase(TestCase):
    def setUp(self):
        video_a = Video.objects.create(title='My title', video_id='abc')
        self.video_a = video_a
        self.obj_a = Playlist.objects.create(title="Random title", video=video_a)
        self.obj_b = Playlist.objects.create(
            title="Random title", 
            state=PublishStateOptions.PUBLISH, 
            video=video_a
            )

    def test_playlist_video(self):
        self.assertEqual(self.obj_a.video, self.video_a)

    def test_video_playlist(self):
        qs = self.video_a.playlist_set.all()
        self.assertEqual(qs.count(),2)

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_valid_title(self):
        title = "Random title"
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(),2)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)
    
    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Playlist.objects.filter(publish_timestamp__lte = now)
        self.assertEqual(qs.count(), 1)
        self.assertTrue(published_qs.exists())
            
    def test_publish_manager(self):
        published_qs = Playlist.objects.all().published() # published from VideoQuerySet
        published_qs_2 = Playlist.objects.published()  # published from VideoManager
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs_2.count(), 1) 