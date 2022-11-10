#### TASK 01 ####
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# - название модели,
# - год выпуска,
# - производителя,
# - объем двигателя,
# - цвет машины,
# - цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Car:

    def __init__(self, model, year, manufacture, volume, color, price):
        self.model = model
        self.year = year
        self.manufacture = manufacture
        self.volume = volume
        self.color = color
        self.price = price

    def showInfo(self):
        print("-" * 45 + " Car Info " + "-" * 45 + f"\nManufacture: {self.manufacture}\nModel: {self.model}"
                                                   f"\nYear: {self.year} Volume: {self.volume} l."
                                                   f"\nColor: {self.color}\nPrice: {self.price} USD")

    def setModel(self, model):
        if 2 <= len(model) < 30:
            self.model = model
        else:
            print("Error! Incorrect model!")

    def setYear(self, year):
        if year is int and 1800 <= year < 2022:
            self.year = year
        else:
            print("Error! Incorrect year!")

    def setManufacture(self, manufacture):
        if 2 <= len(manufacture) < 40:
            self.manufacture = manufacture
        else:
            print("Error! Incorrect manufacture!")

    def setVolume(self, volume):
        if volume is int and 1800 <= volume < 2022:
            self.volume = volume
        else:
            print("Error! Incorrect volume!")

    def setColor(self, color):
        if 3 <= len(color) < 20:
            self.color = color
        else:
            print("Error! Incorrect color!")

    def setPrice(self, price):
        if 0 < price:
            self.price = price
        else:
            print("Error! Incorrect price!")

    def getModel(self):
        return self.model

    def getYear(self):
        return f"Year: {self.year}"

    def getManufacture(self):
        return f"Manufacture: {self.manufacture}"

    def getVolume(self):
        return f"Volume: {self.volume} l."

    def getColor(self):
        return f"Color: {self.color}"

    def getPrice(self):
        return f"Price: {self.price} USD"


renault = Car("Scenic", 2015, "Renault", 2.0, "black", 15000)
renault.showInfo()
renault.setPrice(16000)
print(renault.getPrice())

