#!/usr/bin/python3

''' Prime Game Winner '''


def is_prime(n):
    ''' Checks if a given number is prime '''
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def get_primes(n, primes):
    '''calculates prime numbers '''
    max_prime = primes[-1]
    if n > max_prime:
        for i in range(max_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    '''calculates number of rounds won and returns
    player that won most rounds'''

    wins = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    get_primes(max(nums), primes)

    for round in range(x):
        round_sum = sum((i != 0 and i <= nums[round])
                        for i in primes[:nums[round] + 1])

        if (round_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"

    return None
