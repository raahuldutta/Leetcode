''' Pow(x, n)
Medium

796

1967

Favorite

Share
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25'''

n = 10
x = 2.000
if n < 0:
    x = 1 / x
    n = -n
pow = 1
while n:
    if n & 1:
        pow *= x
    x *= x
    n >>= 1

print(pow)
