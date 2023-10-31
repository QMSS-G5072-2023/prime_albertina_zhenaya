from prime_zea2107 import prime_zea2107
from prime_zea2107.prime_zea2107 import is_prime
import math
import pytest

def test_is_prime():
    input1 = 2
    input2 = 8
    expected = True
    actual = is_prime(input1)
    assert actual == expected