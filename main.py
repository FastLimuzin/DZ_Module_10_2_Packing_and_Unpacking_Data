import json
import pickle

# Задание 1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        return f"{self.brand} {self.model} поехал!"

    def stop(self):
        return f"{self.brand} {self.model} остановился."

    # pickle
    def save_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    # json
    def save_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return Car(**data)


# Задание 2:
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def read(self):
        return f"Читаем книгу '{self.title}' автора {self.author}."

    def get_info(self):
        return f"'{self.title}', {self.author}, {self.year} год."

   
    def save_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    # json через Encoder
    def save_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self, file, cls=BookEncoder)

    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return Book(**data)

class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return obj.__dict__
        return super().default(obj)


# Задание 3
class Stadium:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    def open(self):
        return f"Стадион '{self.name}' открыт!"

    def close(self):
        return f"Стадион '{self.name}' закрыт."

   
    def save_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    #json через Adapter
    def save_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(StadiumAdapter.to_dict(self), file)

    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return Stadium(**data)

class StadiumAdapter:
    @staticmethod
    def to_dict(obj):
        if isinstance(obj, Stadium):
            return {
                "name": obj.name,
                "location": obj.location,
                "capacity": obj.capacity
            }
        raise TypeError("Object is not of type 'Stadium'")


if __name__ == "__main__":
    # Car
    car = Car("Ford", "explorer", 2013)
    car.save_json("car.json")
    loaded_car = Car.load_json("car.json")
    print(loaded_car.drive())

    # Book
    book = Book("Red pill", "Andrey Kurpatov", 2017)
    book.save_json("book.json")
    loaded_book = Book.load_json("book.json")
    print(loaded_book.get_info())

    # Stadium
    stadium = Stadium("Стадион Звезда", "Пермь", 17000)
    stadium.save_json("stadium.json")
    loaded_stadium = Stadium.load_json("stadium.json")
    print(loaded_stadium.open())
