'''
Generate Parentheses
Medium

2553

156

Favorite

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]'''

def generateParanHelper(curr, num_available, num_unclosed):
    if num_available == 0:
        return [curr + ')'*num_unclosed]
    elif num_unclosed == 0:
        return generateParanHelper(curr + '(', num_available - 1,num_unclosed + 1)
    else:
        return generateParanHelper(curr + '(', num_available - 1, num_unclosed + 1) + generateParanHelper(curr + ')', num_available,num_unclosed - 1)
def generateParen(n):
    if n == 0:
        return []
    else:
        return generateParanHelper('',n,0)

print(generateParen(3))

