from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from netflix.db.models import PublishStateOptions
from .models import Video
# Create your tests here.

class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_a = Video.objects.create(title="Random title", video_id='abc')
        self.obj_b = Video.objects.create(title="Random title", state=PublishStateOptions.PUBLISH, video_id='adc')

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_valid_title(self):
        title = "Random title"
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(),2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)
    
    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(publish_timestamp__lte = now)
        self.assertEqual(qs.count(), 1)
        self.assertTrue(published_qs.exists())
            
    def test_publish_manager(self):
        published_qs = Video.objects.all().published() # published from VideoQuerySet
        published_qs_2 = Video.objects.published()  # published from VideoManager
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs_2.count(), 1) 