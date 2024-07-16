# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
# + сумма площин двох екземплярів ксласу
# - різниця площин двох екземплярів ксласу
# == площин на рівність
# != площин на не рівність
# >, < меньше більше
# при виклику метода len() підраховувати сумму сторін

from typing import Self
from abc import ABC, abstractmethod


class Rectangle:
    def __init__(self, side_x: int, side_y: int):
        self.side_x = side_x
        self.side_y = side_y

    def __repr__(self) -> str:
        return f'Rectangle: x = {self.side_x} y = {self.side_y}'

    def __add__(self, other: Self) -> int:
        return (self.side_x * self.side_y) + (other.side_x * other.side_y)

    def __sub__(self, other: Self) -> int:
        return (self.side_x * self.side_y) - (other.side_x * other.side_y)

    def __eq__(self, other: Self) -> bool:
        return self.side_x * self.side_y == other.side_x * other.side_y

    def __ne__(self, other: Self) -> bool:
        return self.side_x * self.side_y != other.side_x * other.side_y

    def __gt__(self, other: Self) -> str:
        if (self.side_x * self.side_y) > (other.side_x * other.side_y):
            return f'{self} square is bigger'
        return f'{self} square is not bigger'

    def __lt__(self, other: Self) -> str:
        if (self.side_x * self.side_y) < (other.side_x * other.side_y):
            return f'{self} square is smaller'
        return f'{self} square is not smaller'

    def __len__(self) -> int:
        return 2 * (self.side_x + self.side_y)


rec1 = Rectangle(5, 10)
rec2 = Rectangle(10, 10)
rec3 = Rectangle(10, 5)

print(rec1)
print(rec2)
print('square sum = ', rec1 + rec2)
print('square sub = ', rec2 - rec1)
print('are squares equal: ', rec1 == rec2)
print('are squares equal: ', rec1 == rec3)
print('are squares NOT equal: ', rec1 != rec2)
print('are squares NOT equal: ', rec1 != rec3)
print(rec1 > rec2)
print(rec2 > rec1)
print(rec1 < rec2)
print(rec2 < rec1)
print('perimeter = ', len(rec1))

print('-' * 50)


# ###############################################################################
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Prince(Human):
    def __init__(self, name: str, age: int, found_shoe: int):
        super().__init__(name, age)
        self.found_shoe = found_shoe

    def find_cinderella(self, girls: list) -> str:
        for cinderella in girls:
            if self.found_shoe == cinderella.shoe_size:
                return f'{cinderella} - is correct cinderella'
        return f'404: cinderella not found'


class Cinderella(Human):
    __count: int = 0

    def __init__(self, name: str, age: int, shoe_size: int):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella._inc_count()

    @classmethod
    def _inc_count(cls):
        cls.__count += 1

    @classmethod
    def get_count(cls) -> int:
        return cls.__count

    def __repr__(self):
        return f'{self.name}, age: {self.age}, shoe size: {self.shoe_size}'


cin1 = Cinderella("Anna", 25, 10)
cin2 = Cinderella("Alice", 30, 8)
cin3 = Cinderella("Eva", 35, 9)
cin4 = Cinderella("Emily", 28, 7)
cin5 = Cinderella("Olivia", 40, 11)
cin6 = Cinderella("Sophia", 199, 6)
cin7 = Cinderella("Isabella", 29, 9)
cin8 = Cinderella("Emma", 32, 8)
cin9 = Cinderella("Mia", 27, 10)
cin10 = Cinderella("Ava", 31, 7)

print('there are', Cinderella.get_count(), 'cinderellas')

prince = Prince('Shrek', 50, 6)
print(prince.find_cinderella([cin1, cin2, cin3, cin4, cin5, cin6, cin7, cin8, cin9, cin10]))


# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають
# є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name, 'book')


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name, 'magazine')


class Main:
    __printable_list: list = []

    @classmethod
    def add(cls, item: Printable):
        if isinstance(item, (Book, Magazine)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()


print('-' * 50)
Main.add(Book('book1'))
Main.add(Book('book2'))
Main.add(Book('book3'))
Main.add(Magazine('magazine1'))
Main.add(Book('book4'))
Main.add(Magazine('magazine11'))
Main.add(Book('book 100500'))
Main.add(Magazine('magazine111'))

Main.show_all_books()
Main.show_all_magazines()
