#!/usr/bin/env python
# coding: utf-8
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

def main():
    # print(smallestMultipleOf(range(1, 11)))
    print(smallestMultipleOf(range(1, 21)))

def smallestMultipleOf(numbers):
    numbers.sort()
    numbers = numbers[::-1]
    multiple = 1
    for number in numbers:
        if multiple % number != 0:
            multiple *= number / greatestDivisor(multiple, number)
    return multiple

def greatestDivisor(number1, number2):
    a = max(number1, number2)
    b = min(number1, number2)
    while a%b != 0:
        temp = b
        b = a%b
        a = temp
    return b

if __name__ == "__main__":
    main()
