#!/usr/bin/env python
# coding: utf-8
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def main():
    # print(sumSquareDifference(range(1, 11)))
    print(sumSquareDifference(range(1, 101)))

def sumSquareDifference(numbers):
    difference = 0
    for number1 in numbers:
        for number2 in numbers:
            if number1 == number2:
                break
            difference += 2*number1*number2
    return difference

if __name__ == "__main__":
    main()
