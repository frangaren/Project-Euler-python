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

# The multiples of 3 under 20 are
#   3, 6, 9, 12, 15, 18
# and they add up to 63, we can also see that
#    3 = 3 * 1
#    6 = 3 * 2
#    9 = 3 * 3
#   12 = 3 * 4
#   15 = 3 * 5
#   18 = 3 * 6
# so
#   3 + 6 + 9 + 12 + 15 + 18 =
#   3*1 + 3*2 + 3*3 + 3*4 + 3*5 + 3*6 =
#   3 * (1 + 2 + 3 + 4 + 5 + 6) =
#   3 * triangular_number(6) = 21 * 3 = 63
# We can also observe that 6 is the number of multiples of 3 below 20.
# This can be calculated as (20 - 1)//3. So, a valid definition of
# sum_multiples_of is
# sum_multiples_of(n, b) = n * triangular_of((b - 1) // n)
def sum_multiples_of(number, upper_bound):
    multiple_count = (upper_bound - 1)//number
    return number * triangular_of(multiple_count)

def triangular_of(number):
    return (number * (number + 1)) // 2

if __name__ == "__main__":
    main()
