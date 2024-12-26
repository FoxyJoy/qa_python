
import pytest

@pytest.fixture(scope="session")
def book_name():
    return 'Мультимышь в деревне Z'

@pytest.fixture(scope="session")
def book_genre():
    return 'Фантастика'

@pytest.fixture(scope="session")
def book_name2():
    return 'Несуществующая книга'

@pytest.fixture(scope="session")
def book_genre2():
    return 'Несуществующий жанр'

@pytest.fixture(scope="session")
def book_genre3():
    return 'Мультфильмы'

@pytest.fixture(scope="session")
def book_name3():
    return 'Холодное полотенце'

@pytest.fixture(scope="session")
def book_name4():
    return 'Венчик'

@pytest.fixture(scope="session")
def book_genre4():
    return 'Ужасы'
