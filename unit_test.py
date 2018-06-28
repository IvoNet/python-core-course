#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import unittest

from cooldata import classes


class MyTests(unittest.TestCase):

    def setUp(self):
        self.emp = classes.Employee("Number", "One")

    def test1(self):
        self.assertEqual("Yes I do", self.emp.work())


if __name__ == '__main__':
    unittest.main()
