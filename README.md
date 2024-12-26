### Проверка на добавление книги
```
def test_add_new_book(self):
```

### Проверка на добавление книги с пустым именем
```
def test_add_new_book_empty_name(self):
```

### Проверка на добавление книги с именем более 40 смиволов
```
def test_add_new_book_large_name(self):
```

### устанавливаем книге жанр
```
def test_set_book_genre(self, book_name, book_genre):
```

### Проверка на установку жанра для несуществующей книги
```
def test_set_book_genre_non_existent_book(self, book_name2, book_genre):
```

### Проверка на несуществующий жанр книги
```
def test_set_book_genre_non_existent_book_genre(self, book_name, book_genre2):
```

### получаем жанр книги по её имени
```
def test_get_book_genre(self, book_name, book_genre):
```
    
### получаем жанр книги не пустой
```
def test_get_book_genre_not_empty(self, book_name, book_genre):
```

### выводим список книг с определённым жанром
```
def test_get_books_with_specific_genre(self, book_name, book_genre):
def test_get_books_with_specific_genre_2(self, book_name3, book_genre3):
```

### Проверка на несуществующий жанр
```
def test_get_books_with_specific_genre_dictionary(self, book_genre2):
```

### получаем словарь books_genre
```
def test_get_books_genre(self):
def test_get_books_genre_not_dictionary(self):
```

### возвращаем книги, подходящие детям
```
def test_get_books_for_children_list(self):
def test_get_books_for_children_not_list(self):
def test_get_books_for_children_true(self, book_name3, book_genre3):
def test_get_books_for_children_false(self, book_name4, book_genre4):
```

### добавляем книгу в Избранное
```
def test_add_book_in_favorites(self, book_name):
```

### добавляем книгу в Избранное несуществующую
```
def test_add_book_in_favorites_not_in_favorites(self, book_name2):
```

### добавляем еще одну имеющуюся книгу в избранное
```
def test_add_book_in_favorites_two_same_in_favorites(self, book_name4):
```

### удаляем книгу из Избранного
```
def test_delete_book_from_favorites(self, book_name):
```

### удаляем книгу несуществующую
```
def test_delete_book_from_favorites_non_existent_book(self, book_name2):
```

### получаем список Избранных книг
```
def test_get_list_of_favorites_books(self, book_name4):
```