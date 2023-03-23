#!/usr/bin/python3
'''Pascal's triangle'''


def pascal_triangle(n):
    '''Returns a 2d list of integers representing
    the Pascal's triangle of a given integer.
    '''
    result = []
    if (n <= 0):
        return result
    for i in range(n):
        current = []
        for x in range(i+1):
            if (x == 0 or x == i):
                current.append(1)
            elif (i > 0 and x > 0):
                current.append(result[i-1][x-1] + result[i-1][x])
        result.append(current)
    return result
