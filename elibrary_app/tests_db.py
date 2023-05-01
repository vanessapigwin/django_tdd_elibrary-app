from django.test import TestCase
from elibrary_app.models import Catalogue

class CatalogueModelTests(TestCase):

    def setUp(self):
        self.book = Catalogue(
            title = 'first title',
            ISBN = '978-3-16-420',
            author = 'Winwin Chicken',
            price = '4.20',
            availability = 'True'
        )

    def test_create_book(self):
        self.assertIsInstance(self.book, Catalogue)

    def test_str_representation(self):
        self.assertEquals(str(self.book), 'first title')

    def test_save_and_retrieve_book(self):
        first_book = Catalogue()
        first_book.title = 'first title'
        first_book.ISBN = '12344556'
        first_book.author = 'Bart Dog'
        first_book.price = '6.90'
        first_book.availability = 'True'
        first_book.save()

        second_book  = Catalogue()
        second_book.title = 'second title'
        second_book.ISBN = '456789'
        second_book.author = 'chichiw taba'
        second_book.price = '420.69'
        second_book.availability = 'False'
        second_book.save()

        saved_books = Catalogue.objects.all()
        self.assertEqual(saved_books.count(), 2)

        first_saved_book = saved_books[0]
        second_saved_book = saved_books[1]
        self.assertEqual(first_saved_book.title, 'first title')
        self.assertEqual(second_saved_book.author, 'chichiw taba')