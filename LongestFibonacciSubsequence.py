''' A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
'''

A = [1,2,3,4,5,6,7,8]


maxLen = 0

for i in range(len(A)):
    for j in range(i+1, len(A)):
        x = A[j]
        y = A[i] + A[j]
        length = 2
        while y in A:
            z = x + y
            x = y
            y = z
            length = length + 1
            maxLen = max(maxLen,length)
print(maxLen if maxLen >=3 else 0)



