from double import DoublyLinkedList
from Empty import Empty

from time import time


class Animal:
    def __init__(self, name):
        self.name = name
        self.time_stamp = time()


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


class AnimalQueue:
    def __init__(self):
        self._cats = DoublyLinkedList.DoublyLinkedList()
        self._dogs = DoublyLinkedList.DoublyLinkedList()

    def get_dog(self):
        if self._dogs.is_empty():
            raise Empty('The Queue is empty')
        current_dog = self._dogs.tail.prev
        self._dogs.delete_node(current_dog)
        return current_dog.element.name

    def get_cat(self):
        if self._cats.is_empty():
            raise Empty('The Queue is empty')
        current_cat = self._cats.tail.prev
        self._cats.delete_node(current_cat)
        return current_cat.element.name

    def get_oldest(self):
        current_dog = self._dogs.tail.prev
        current_cat = self._cats.tail.prev
        result = None

        if current_dog.element.time_stamp < current_cat.element.time_stamp:
            result = current_dog
            self._dogs.delete_node(result)
        else:
            result = current_cat
            self._cats.delete_node(result)

        return result.element.name


    def add_dog(self, name):
        new_dog = Dog(name)
        self._dogs.add_first(new_dog)

    def add_cat(self, name):
        new_cat = Cat(name)
        self._cats.add_first(new_cat)


#test code

animals = AnimalQueue()
animals.add_cat('pussy1')
animals.add_dog('terry2')

animals.add_cat('pussy2')
animals.add_cat('pussy3')

animals.add_dog('terry1')
animals.add_dog('terry2')
animals.add_dog('terry3')

print(animals.get_dog())
print(animals.get_cat())
print(animals.get_cat())
print(animals.get_oldest())



