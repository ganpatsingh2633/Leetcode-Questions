class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        def dfs(i,j,k):
            if k == len(word):
                return True
            if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != word[k]:
                return False
            t = board[i][j]
            board[i][j] = '#'
            found = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1))
            board[i][j] = t
            return found
        for i in range(r):
            for j in range(c):
                if dfs(i,j,0):
                    return True
        return False
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         rows, cols = len(board), len(board[0])

#         def dfs(i: int, j: int, k: int) -> bool:
#             if k == len(word):
#                 return True
#             if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
#                 return False

#             temp = board[i][j]
#             board[i][j] = '#'  # mark visited

#             found = (dfs(i + 1, j, k + 1) or
#                      dfs(i - 1, j, k + 1) or
#                      dfs(i, j + 1, k + 1) or
#                      dfs(i, j - 1, k + 1))

#             board[i][j] = temp  # backtrack
#             return found

#         for i in range(rows):
#             for j in range(cols):
#                 if dfs(i, j, 0):
#                     return True
#         return False










        # a = Counter(word)
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] in a:
        #             a[board[i][j]] -= 1
        # for k, v in a.items():
        #     if v > 0:
        #         return False
        # return True
    
                   