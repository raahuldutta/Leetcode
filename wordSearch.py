'''  Word Search
Medium

1610

77

Favorite

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCD"


def dfs(board, row, col, word):
    if len(word) == 0:
        return True
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
        return False
    
    temp = board[row][col]
    board[row][col] = '@'

    result = dfs(board, row+1, col, word[1:]) or dfs(board, row-1, col, word[1:]) or dfs(board, row, col+1, word[1:]) or dfs(board, row, col-1, word[1:])
    board[row][col] = temp
    return result

for i in range(len(board)):
    for j in range(len(board[0])):
        if dfs(board, i, j, word):
            print(word)


