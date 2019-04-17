''' Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].'''

phone = {'2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
output = []
def backtrack(combinations, next_digits):
    if len(next_digits) == 0:
        output.append(combinations)
    else:
        for i in phone[next_digits[0]]:
            backtrack(combinations + i,next_digits[1:])

backtrack('',['2','3'])
print(output)

        