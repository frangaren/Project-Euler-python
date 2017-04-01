#!/usr/bin/env python
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    print(sum(getMultiplesOf([3, 5], 1000)));

def getMultiplesOf(numbers, maximum):
    lst = list()
    for n in numbers:
        x = 1
        m = x*n
        while m < maximum:
            if not (m in lst):
                lst.append(x*n)
            x += 1;
            m = x*n
    #lst.sort()
    return lst

if __name__ == "__main__":
    main()
