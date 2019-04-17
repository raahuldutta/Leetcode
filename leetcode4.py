''' Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
'''

a = matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
#a = matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
ansMatrix = []

r1 = 0
c1 = 0
r2 = len(a) - 1
c2 = len(a[0]) - 1

while r1 <= r2 and c1 <= c2:
    for i in range(c1,c2 + 1):
        ansMatrix.append(a[r1][i])
    for i in range(r1+1,r2+1):
        ansMatrix.append(a[i][c2])
    if r1< r2 and c1< c2:
        for i in range(c2-1,c1,-1):
            ansMatrix.append(a[r2][i])
        for i in range(r2,r1, -1):
            ansMatrix.append(a[i][c1])
    r1 = r1 + 1
    c1 = c1 + 1
    r2 = r2 - 1
    c2 = c2 - 1

[0,1,0,3,12]
1,0,0,3,12


1,3,12
0-2
1-1
3-1
12-1
1312


    
    

print('raahul')


