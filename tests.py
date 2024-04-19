import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_book_add_book_in_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Сто лет одиночества')

        assert 'Сто лет одиночества' in collector.get_books_genre()

    @pytest.mark.parametrize(
        'book,genre',
        [
            ['Сто лет одиночества', 'Фантастика']
        ]
    )
    def test_set_book_genre_name_genre_set_genre(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_genre()[book] == genre

    @pytest.mark.parametrize(
        'book,genre',
        [
            ['Ведьмак', 'Фантастика'],
            ['Властелин колец', 'Фантастика'],
            ['Рассказы о Шерлоке Холмсе', 'Детективы']
        ]
    )
    def test_get_books_with_specific_genre_genre_list_of_books(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert book in collector.get_books_with_specific_genre(genre)

    def test_get_books_genre_book_books_genre_type_dict(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        assert isinstance(collector.get_books_genre(), dict)


    @pytest.mark.parametrize(
        'books,genre',
        [
            [['Ведьмак', 'Властелин колец', 'Песнь льда и пламени'], 'Фантастика'],
            [['Дневник Домового. Рассказы с чердака', 'Как я встретил вашу няню'], 'Комедии'],
            [['Дядя Федор, пёс и кот', 'Что делать, если ваш кот хочет вас убить'], 'Мультфильмы']
        ]
    )
    def test_get_books_for_children_book_genre_books_for_children(self, books, genre):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == books

    @pytest.mark.parametrize(
        'books,genre',
        [
            [['Оно', 'Сияние'], 'Ужасы'],
            [['Рассказы о Шерлоке Холмсе', 'Тринадцатая сказка'], 'Детективы'],
        ]
    )
    def test_get_books_for_children_book_genre_get_empty_list(self, books, genre):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_book_add_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Рассказы охотника')
        collector.add_book_in_favorites('Рассказы охотника')

        assert 'Рассказы охотника' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_delete_is_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Рассказы охотника')
        collector.add_book_in_favorites('Рассказы охотника')
        collector.delete_book_from_favorites('Рассказы охотника')

        assert 'Рассказы охотника' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book', ['Рассказы охотника', 'Тринадцатая сказка', 'Как я встретил вашу няню', 'Рассказы о Шерлоке Холмсе'])
    def test_get_list_of_favorites_books_book_get_list_books(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()




