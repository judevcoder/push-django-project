from clients.models import ClientProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from models import Segment
from pushmonkey.models import Device, WebServiceDevice
import json

c = Client()

class SegmetsTests(TestCase):

    def test_retrieving_segments(self):

      user = User.objects.create_user('john', 
        'lennon@thebeatles.com', 
        'johnpassword')
      profile = ClientProfile.objects.create(
        website_push_id = 'web.com.pushmonkey.1', 
        user = user)
      seg1 = Segment.objects.create(account_key = "abc", client = profile, name = "Seg 1")
      seg2 = Segment.objects.create(account_key = "abc", client = profile, name = "Seg 2")
      data = {"endpoint": "xyz"}
      res = c.post(reverse('segments', args = ["abc"]), data)
      json_res = json.loads(res.content)

      self.assertEqual(len(json_res["segments"]), 2)
      self.assertContains(res, "Seg 2")
      self.assertContains(res, "<h3")
