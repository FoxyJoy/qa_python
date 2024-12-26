from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2
    
    def test_add_new_book_add_same_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_large_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби, Гордость')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    def test_set_book_genre_non_existent_book(self, book_name2, book_genre):
        collector = BooksCollector()
        collector.set_book_genre(book_name2, book_genre)
        assert collector.get_book_genre(book_name2) is None

    def test_set_book_genre_non_existent_book_genre(self, book_name, book_genre2):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre2)
        assert collector.get_book_genre(book_name) == ''

    def test_get_book_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre
        
    def test_get_book_genre_not_empty(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) != ''

    def test_get_books_with_specific_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        book = collector.get_books_with_specific_genre(book_genre)
        assert book_name in book

    def test_get_books_with_specific_genre_2(self, book_name3, book_genre3):
        collector = BooksCollector()
        collector.add_new_book(book_name3)
        collector.set_book_genre(book_name3, book_genre3)

        book = collector.get_books_with_specific_genre(book_genre3)
        assert book_name3 != book

    def test_get_books_with_specific_genre_dictionary(self, book_genre2):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre(book_genre2) == []

    def test_get_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_genre_not_dictionary(self):
        collector = BooksCollector()
        assert collector.get_books_genre() != []

    def test_get_books_for_children_list(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_not_list(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() != {}

    def test_get_books_for_children_true(self, book_name3, book_genre3):
        collector = BooksCollector()
        collector.add_new_book(book_name3)
        collector.set_book_genre(book_name3, book_genre3)

        books_for_children = collector.get_books_for_children()
        assert book_name3 in books_for_children

    def test_get_books_for_children_false(self, book_name4, book_genre4):
        collector = BooksCollector()
        collector.add_new_book(book_name4)
        collector.set_book_genre(book_name4, book_genre4)

        books_for_children = collector.get_books_for_children()
        assert book_name4 not in books_for_children

    def test_add_book_in_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    def test_add_book_in_favorites_not_in_favorites(self, book_name2):
        collector = BooksCollector()
        collector.add_book_in_favorites(book_name2)
        assert book_name2 not in collector.favorites

    def test_add_book_in_favorites_two_same_in_favorites(self, book_name4):
        collector = BooksCollector()
        collector.add_new_book(book_name4)
        collector.add_book_in_favorites(book_name4)
        collector.add_book_in_favorites(book_name4)
        assert collector.favorites.count(book_name4) == 1

    def test_delete_book_from_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites

    def test_delete_book_from_favorites_non_existent_book(self, book_name2):
        collector = BooksCollector()
        collector.delete_book_from_favorites(book_name2)
        assert book_name2 not in collector.favorites

    def test_get_list_of_favorites_books(self, book_name4):
        collector = BooksCollector()
        collector.add_new_book(book_name4)
        collector.add_book_in_favorites(book_name4)
        assert collector.get_list_of_favorites_books() != []
