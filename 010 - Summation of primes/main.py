#!/usr/bin/env python
# coding: utf-8
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from itertools import takewhile
from math import floor, sqrt

def main():
    print(sumOfPrimesBelow(2000000))

def sumOfPrimesBelow(number):
    return sum(takewhile(lambda x: x < number, primes()))

def primes():
    yield 2
    yield 3
    yield 5
    yield 7
    n = 11
    while 1:
        if n % 2 == 0:
            n += 1
            continue
        elif n % 3 == 0:
            pass
        else:
            if primeCheck(n):
                yield n
        n += 2

def primeCheck(n):
    r = floor(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True

if __name__ == "__main__":
    main()
