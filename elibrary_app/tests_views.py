from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.urls.base import resolve
from elibrary_app.views import home
from elibrary_app.models import Catalogue


class CatalogueViewTests(TestCase):

    def test_book_list_view(self):
        """
            A test method to show that the books we created are shown correctly on our template.
        """

        Book_1 = Catalogue.objects.create(
            title='Django for Beginners (2018)', 
            ISBN='978-1-60309-0', 
            author='John Doe',
            price=9.99,
            availability='true'
        )

        Book_2 = Catalogue.objects.create(
            title='Django for Professionals (2020)', 
            ISBN='978-1-60309-3', 
            author='Mary Doe',
            price=11.99,
            availability='false'
        )

        response = self.client.get(reverse('home'))

        self.assertIn('Django for Professionals (2020)', response.content.decode())
        self.assertIn('John Doe', response.content.decode())
        self.assertIn('978-1-60309-3', response.content.decode())


class ElibraryURLsTest(TestCase):
    "Test the catalogue URLs"

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home)