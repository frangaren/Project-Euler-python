#!/usr/bin/env python
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from itertools import islice
from math import floor, sqrt

def main():
    print(lastPrimeFactor(600851475143))

def lastPrimeFactor(n):
    lastFactor = 1
    primeGenerator = primes()
    r = floor(sqrt(n))
    factor = primeGenerator.next()
    while n > 1 and factor < r:
        if (n % factor == 0):
            lastFactor = factor
            n /= factor
        else:
            factor = primeGenerator.next()
    return max(lastFactor, n)

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
