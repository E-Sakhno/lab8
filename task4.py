#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getInput():
    inp = input("Введите символы: ")
    return inp


def testInput(value):
    try:
        int(value)
        return True
    except:
        return False


def strToInt(value):
    return int(value)


def printInt(value):
    print(value)


if __name__ == '__main__':
    a = getInput()
    if testInput(a):
        a_int = strToInt(a)
        printInt(a_int)
