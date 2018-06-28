#!/usr/bin/env python
#  -*- coding: utf-8 -*-


from cooldata.classes import Person


class CrookException(Exception):
    def __init__(self, message) -> None:
        self.message = message


class Crook(Person):
    def steal(self):
        raise CrookException("I stole something")


if __name__ == '__main__':
    crook = Crook("Bad", "guy")
    print(crook)

    try:
        crook.steal()
    except CrookException as e:
        print(e.message)

    crook.steal()
