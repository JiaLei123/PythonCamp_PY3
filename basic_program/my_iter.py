#!/usr/bin/python
# coding=utf-8

class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


if __name__ == "__main__":
    fibs = Fibs()
    for fib in fibs:
        if fib > 1000:
            break
        print(fib)
