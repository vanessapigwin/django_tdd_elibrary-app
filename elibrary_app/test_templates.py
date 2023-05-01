from django.test import TestCase
from django.urls import reverse

class CatalogueTemplateTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('home'))
    
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'elibrary_app/index.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'E-Library Application')