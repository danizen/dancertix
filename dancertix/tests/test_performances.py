from django.test import TestCase

from dancertix.models import Performance

class TestPerformances(TestCase):

    def test_performances(self):
        actual_count = Performance.objects.filter(venue__name='F. Scott Fitzgerald Theatre').count()
        assert actual_count == 6
