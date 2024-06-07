#!/usr/bin/python3
"""module contains a function that determines the feweest number
of coins needed to make change where
the list of coins is given as the first argument and the amount
is given as the second argument, the function returns -1 if it is not possible
to give change."""


def makeChange(coins, total):
    """function that determines the feweest number
    of coins needed to make change where
    the list of coins is given as the first argument and the amount
    is given as the second argument, the function returns -1 if it is not
    possible to give change."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        if total >= coin:
            coin_count += total // coin
            total = total % coin
    if total == 0:
        return coin_count
    return -1
