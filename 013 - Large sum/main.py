#!/usr/bin/env python
# coding: utf-8
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
# (Look at numbers.txt for the numbers)

def main():
    numbers = loadNumbers()
    print(findFirstDigitsOfSum(numbers, 10))

def loadNumbers():
    numbers = list()
    with open("numbers.txt", "r") as numbersFile:
        for line in numbersFile:
            numbers.append(list())
            for digit in line:
                if digit.isdigit():
                    numbers[len(numbers) - 1].append(int(digit))
    return numbers

def findFirstDigitsOfSum(numbers, digits):
    numberLength = len(numbers[0])
    summation = sumVectors(*numbers)
    carry = 0
    for i in xrange(numberLength - 1, -1, -1):
        summation[i] += carry
        carry = summation[i] / 10
        summation[i] %= 10
    while carry > 0:
        summation.insert(0, carry%10)
        carry /= 10
    return getNumberFromDigits(summation[:digits])

def transpose(m):
    return list(map(list, zip(*m)))

def getDigits(number):
    digits = list()
    while number > 0:
        digits.append(number % 10)
        number /= 10
    digits.reverse()
    return digits

def getNumberFromDigits(digits):
    number = 0
    for digit in digits:
        number *= 10
        number += digit
    return number

def sumVectors(*args):
    return map(sum, transpose(args))

if __name__ == "__main__":
    main()
