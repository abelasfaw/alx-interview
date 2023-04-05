#!/usr/bin/python3
"""Minimum opertions"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations
    needed to result in exaclty n H
    characters in the file
    """
    ops = 0

    if n <= 1:
        return ops

    for i in range(2, n + 1):
        while (n % i == 0):
            ops = ops + i
            n = n / i
            if n < i:
                break
    return ops
