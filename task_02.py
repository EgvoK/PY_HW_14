#### TASK 02 ####
# Реализуйте класс «Книга».
# Необходимо хранить в полях класса:
# - название книги,
# - год выпуска,
# - издателя,
# - жанр,
# - автора,
# - цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# К уже реализованному классу «Книга» добавьте конструктор, а также необходимые перегруженные методы.

class Book:

    __price = 0

    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.__price = price

    def __str__(self):
        return f"{'-' * 40} Book Info {'-' * 40}\nTitle: {self.title}\nAuthor: {self.author}" \
               f"\nPublisher: {self.publisher}\nYear: {self.year}\nGenre: {self.genre}\nPrice: {self.__price}$"

    @staticmethod
    def printError():
        print("Error! Incorrect data!")

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, publisher):
        self.publisher = publisher

    def getGenre(self):
        return self.genre

    def setGenre(self, genre):
        self.genre = genre

    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if 1 < price < 100:
            self.__price = price
        else:
            Book.printError()


newBook = Book("451° Fahrenheit", 2008, "PH World", "Prose", "Ray Bradbury", 9.99)
newBook.price = 15
print(newBook)
