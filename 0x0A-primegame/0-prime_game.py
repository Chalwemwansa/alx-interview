#!/usr/bin/python3
""" this module contains a function that finds a winner of a prime game
    where two players maria and ben play"""


primes = [2, 3]


def genPrimes(max):
    """this is the function that generates primes when passed a max and
    appends them to the primes list"""
    global primes
    for num in range(primes[-1] + 1, max + 1):
        prime = True
        for divider in range(2, (num // 2) + 1):
            if (num % divider == 0 and not (num == divider)):
                prime = False
                break
        if (prime):
            primes.append(num)


def isWinner(x, nums):
    """the actual function that checks who the winner is and returns
    the name of the winner"""
    maria = 0
    ben = 0
    round = 0
    for num in nums:
        if (round < x):
            turn = 'maria'
            winner = False
            if (primes[-1] + 1 < num):
                genPrimes(num)
            for prime in primes:
                if (prime > num):
                    if (turn == 'maria'):
                        ben += 1
                    else:
                        maria += 1
                    winner = True
                    break
                if (prime == primes[-1] and num == primes[-1]):
                    if (turn == 'maria'):
                        maria += 1
                    else:
                        ben += 1
                    winner = True
                    break
                if (turn == 'maria'):
                    turn = 'ben'
                else:
                    turn = 'maria'
            if (not winner):
                if (turn == 'maria'):
                    ben += 1
                else:
                    maria += 1
            round += 1
    if (maria == ben):
        return None
    if (maria > ben):
        return 'maria'
    return 'ben'
