#!/usr/bin/env python3
# coding: utf-8

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    sum_multiples_below_10 = sum_multiples_of(3, 10) + \
        sum_multiples_of(5, 10) - sum_multiples_of(15, 10)
    sum_multiples_below_1000 = sum_multiples_of(3, 1000) + \
        sum_multiples_of(5, 1000) - sum_multiples_of(15, 1000)
    print(f"The multiples of 3 and 5 below 10 add up to " \
        f"{sum_multiples_below_10}.")
    print(f"The multiples of 3 and 5 below 1000 add up to " \
        f"{sum_multiples_below_1000}.")

def sum_multiples_of(number, upper_bound):
    multiple_count = (upper_bound - 1)//number
    return (number * multiple_count * (multiple_count + 1)) // 2

if __name__ == "__main__":
    main()
