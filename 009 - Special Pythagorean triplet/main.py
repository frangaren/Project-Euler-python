#!/usr/bin/env python
# coding: utf-8
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def main():
    (a, b, c) = pythagoreanTriplet(1000)
    print(a*b*c)

def pythagoreanTriplet(total):
    for a in range(1, total):
        for b in range(a, total):
            c = total - a - b
            if c < b:
                break
            elif a*a + b*b == c*c:
                return (a, b, c)

if __name__ == "__main__":
    main()
