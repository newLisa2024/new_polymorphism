# Создайте класс Author и класс Book. Класс Book должен использовать
# композицию для включения автора в качестве объекта.

class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def get_info_book(self):
        print(f'{self.title} - {self.author.name} {self.author.surname}')

author = Author('Александр', 'Пушкин')
book = Book('Евгений Онегин', author)

print(book.title)
print((book.author.name) + ' ' + (book.author.surname))


book.get_info_book()

