#!/usr/bin/env python
#  -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.foo = 4

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.surname)


class Employee(Person):
    def work(self):
        return "Yes I do"


if __name__ == '__main__':
    person1 = Person("Ivo", "Woltring")
    print(type(person1))

    # person1.name = "Foo"
    # person1.foo = 5
    # print(person1)

    emp = Employee("Cees", "Timmerman")
    print(type(emp))
    if type(emp) == Employee:
        print("YUP")
    # print(emp)
    # print(emp.work())
