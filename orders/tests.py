from django.test import TestCase
from .models import Order
from django.urls import reverse

# Create your tests here.


class OrderModelTest(TestCase):

    def setUp(self):
        Order.objects.create(username='bhautik')

    def test_text_content(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.username}'
        self.assertEqual(expected_object_name, 'bhautik')


class HomePageViewTest(TestCase):

    def setUp(self):
        Order.objects.create(username='bhautik')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/order')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('order'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('order'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'order_list.html')
