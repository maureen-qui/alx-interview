#!/usr/bin/python3
"""
Change comes from within
"""
import sys


def minCoins(coins, m, V): 
    """ recursive """
    # base case 
    if (V == 0): 
        return 0

    # Initialize result 
    res = sys.maxsize 
      
    # Try every coin that has smaller value than V 
    for i in range(0, m): 
        if (coins[i] <= V): 
            sub_res = minCoins(coins, m, V-coins[i]) 

            # Check for INT_MAX to avoid overflow and see if 
            # result can minimized 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1

    return res 

def makeChange(coins, total):
    """
    ********************************************
    ****determine the fewest number of coins****
    *******needed to meet a given amount********
    ********************************************
    @coins: is a list of the values of the coins
            in the possession
    @total: given amount
    Return:
            fewest number of coins needed to meet total
            *** If total is 0 or less, return 0
            *** If total cannot be met by any number
                of coins you have, return -1
    """
    m = len(coins) 

    return minCoins(coins, m, total)


print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange([1], 2))

print(makeChange([1,2,5], 11))
