''' 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
'''



stack = []
mapping = {'}':'{', ']':'[', ')':'('}

bracket = '(((({[]))))'

for char in bracket:
    if char in mapping:
        top_element = stack.pop()
        if top_element != mapping[char]:
            print('lost')

    else:
        stack.append(char)
