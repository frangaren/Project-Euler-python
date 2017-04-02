#!/usr/bin/env python
# coding: utf-8
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def main():
    print(longestCollatzUnder(1000000))

def longestCollatzUnder(number):
    buffer = dict()
    maxNumber = 1
    maxLength = 1
    for i in xrange(2, number):
        length = collatzCount(i, buffer)
        if length > maxLength:
            maxNumber = i
            maxLength = length
    return (maxNumber, maxLength)

def collatzCount(number, buffer = dict()):
    if number == 1:
        return 1
    try:
        return buffer[number]
    except KeyError:
        n = number
        count = 1
        if n % 2: # Odd
            count += collatzCount(3*n + 1, buffer)
        else: # Even
            count += collatzCount(n/2, buffer)
        buffer[n] = count
        return count

if __name__ == "__main__":
    main()
