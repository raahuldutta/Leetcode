''' You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1'''


import sys 

def minCoins(coins, m, V):
    if V == 0:
        return 0
    res = sys.maxsize
    for i in range(m):
        if coins[i] <= V:
            sub_res = minCoins(coins, m, V - coins[i])
            if sub_res + 1 < res:
                res = sub_res+ 1
    return res


# Driver program to test above function 
coins = [9, 6, 5, 1] 
m = len(coins) 
V = 11
print("Minimum coins required is",minCoins(coins, m, V)) 

# This code is contributed by 
# Smitha Dinesh Semwal 



