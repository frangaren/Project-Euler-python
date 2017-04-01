#!/usr/bin/env python
# coding: utf-8
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    # print(largestPalindromeProduct(2))
    print(largestPalindromeProduct(3))

def largestPalindromeProduct(numberLength):
    largestNumber = 10 ** numberLength - 1
    lowestNumber = 10 ** (numberLength - 1) - 1
    maximumPalindrome = -1
    for i in xrange(largestNumber, lowestNumber, -1):
        for j in xrange(largestNumber, i, -1):
            number = i*j
            if number > maximumPalindrome and isPalindrome(number):
                maximumPalindrome = number
    if (maximumPalindrome == -1):
        return largestPalindromeProduct(numberLength - 1)
    else:
        return maximumPalindrome

def isPalindrome(number):
    digitList = numberToDigitList(number)
    return digitList == digitList[::-1]

def numberToDigitList(number):
    digitList = list()
    while number > 0:
        digitList.append(number % 10)
        number /= 10
    return digitList

if __name__ == "__main__":
    main()
