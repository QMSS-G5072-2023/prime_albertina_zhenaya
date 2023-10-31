import math

"""
Determines whether or not the number is a prime number.

Parameters
----------
n : an integer

Returns
-------
True if the number is a prime number, False otherwise


Examples
--------
>>> from prime_zea2107 import is_prime
>>> is_prime(2)
>>> [True]

"""


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

