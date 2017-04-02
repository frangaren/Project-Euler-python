#!/usr/bin/env python
# coding: utf-8
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred
# divisors?

from functools import reduce
from itertools import count, dropwhile
from math import floor, sqrt
from operator import mul

def main():
    #print(getTriangularWithDivisors(5))
    print(getTriangularWithDivisors(500))

def getTriangularWithDivisors(number):
    buffer = dict()
    triangularGenerator = triangularNumbers()
    f = lambda x: len(getDivisorsOf(buffer, x)) < number
    n = dropwhile(f, triangularGenerator).next()
    return n

def triangularNumbers():
    number = 0
    for i in count(1):
        number += i
        yield number

def prod(factors):
    return reduce(mul, factors, 1)

def getSublistsOf(lst):
    if len(lst) == 0:
        return [[]]
    else:
        x = lst[0]
        xs = lst[1:]
        ys = getSublistsOf(xs)
        return ys + [[x] + y for y in ys]

def getDivisorsOf(buffer, number):
    factors = getFactorsOf(buffer, number)
    factorsCombinations = getSublistsOf(factors)
    divisors = set(map(prod, factorsCombinations))
    return divisors

def getFactorsOf(buffer, number):
    try:
        return buffer[number][:]
    except KeyError:
        if number == 1:
            return list([1])
        else:
            r = int(floor(sqrt(number)))
            for x in xrange(r, 1, -1):
                if (number % x == 0):
                    factors  = getFactorsOf(buffer, x)
                    factors += getFactorsOf(buffer, number/x)
                    buffer[number] = factors
                    return factors[:]
            return list([number])

if __name__ == "__main__":
    main()