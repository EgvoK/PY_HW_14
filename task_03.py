#### TASK 03 ####
# Реализуйте класс «Стадион».
# Необходимо хранить в полях класса:
# - название стадиона,
# - дату открытия,
# - страну,
# - город,
# - вместимость.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# К уже реализованному классу «Стадион» добавьте конструктор, а также необходимые перегруженные методы.

class Stadium:

    __price = 0

    def __init__(self, caption, date, country, city, capacity):
        self.caption = caption
        self.date = date
        self.country = country
        self.city = city
        self.__capacity = capacity

    def __str__(self):
        return f"{'-' * 40} Stadium Info {'-' * 40}\nCaption: {self.caption}\nOpening date: {self.date}" \
               f"\nCountry: {self.country}\nCity: {self.city}\nCapacity: {self.__capacity}"

    @staticmethod
    def printError():
        print("Error! Incorrect data!")

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if 1 < capacity < 1000000:
            self.__capacity = capacity
        else:
            Stadium.printError()


newStadium = Stadium("Metallist Stadium", "12.09.1926", "Ukraine", "Kharkiv", 40003)
newStadium.capacity = 150000
print(newStadium)

