#!/usr/bin/env python
# coding: utf-8
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?

from itertools import islice
from math import floor, sqrt

def main():
    print(getNthPrime(10001))

def getNthPrime(n):
    return islice(primes(), n - 1, n).next()

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
