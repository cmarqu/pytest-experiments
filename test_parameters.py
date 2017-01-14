#! /usr/bin/env python3

import pytest

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return str(n)


@pytest.mark.parametrize('n, result', [
    (1, '1'),
    (3, 'fizz'),
    (5, 'buzz'),
    (6, 'fizz'),
    (15, 'fizzbuzz'),
    (16, '16'),
])
def test_fizzbuzz(n, result):
    assert fizzbuzz(n) == result
