#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (_type_): _description_
        total (_type_): _description_

    Returns:
        _type_: _description_
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
