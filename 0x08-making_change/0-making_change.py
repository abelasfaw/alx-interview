#!/usr/bin/python3
'''minimum coin needed'''


def makeChange(coins, total):
    n = len(coins)
    if (total <= 0):
        return 0
    remainder = total
    coins_ascending = sorted(coins, reverse=True)
    count = 0
    index = 0
    while(remainder > 0):
        if(index >= n):
            return -1
        if (remainder - coins_ascending[index] >= 0):
            remainder -= coins_ascending[index]
            count += 1
        else:
            index += 1
    return count
