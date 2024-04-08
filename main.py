# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных
# и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для
# `ZooKeeper` и `heal_animal()` для `Veterinarian`).

import json

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        print(f'{self.name} кушает')


class Bird(Animal):
    def make_sound(self):
        print('чирик-чирик')

class Mammal(Animal):
    def make_sound(self):
        print('гав-гав')

class Reptile(Animal):
    def make_sound(self):
        print('шшсшшсшшс')

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк')
    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f'Сотрудник {new_staff} добавлен в сотрудники зоопарка')

class ZooKeeper():
    def feed_animal(self, animal):
        print(f'Сотрудник кормит {animal.name}')

class Veterinarian():
    def heal_animal(self, animal):
        print(f'Ветеринар лечит {animal.name}')

bird1 = Bird('птица', 10)
mammal1 = Mammal('собака', 20)
reptile1 = Reptile('ящерица', 30)

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)
zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

animals = [bird1, mammal1, reptile1]
animal_sound(zoo.animals)

keeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)

