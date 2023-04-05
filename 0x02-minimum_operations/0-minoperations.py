#!/usr/bin/python3
"""Minimum opertions"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations
    needed to result in exaclty n H
    characters in the file
    """
    character_count = 1
    copy_ops = 0
    paste_ops = 0

    while character_count < n:
        if (n % character_count == 0):
            copy_ops += 1
            copied = character_count
        paste_ops += 1
        character_count += copied
    return copy_ops + paste_ops
