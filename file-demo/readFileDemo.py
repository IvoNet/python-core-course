#!/usr/bin/env python
#  -*- coding: utf-8 -*-


with open("random.txt") as fi:
    contents = fi.readlines()
    print(contents)
    if len(contents) > 5:
        print(contents[3])
    for line in contents:
        print(line.replace("the", "THEEEEEEEE"))


