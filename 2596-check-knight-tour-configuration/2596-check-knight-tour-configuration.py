class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0 : return False
        n = len(grid) 
        direct = [
        (1,-2), (-1,-2), (-2,-1), (-2,1),
        (-1,2), (1,2), (2,1), (2,-1)]
        def backtrack(r,c, idx):
            if grid[r][c] == n * n - 1:
                return True
            if grid[r][c] == '#':
                return False
            for dx, dy in direct:
                x, y = r+dx , c + dy
                if 0 <= x < n and 0 <= y < n and grid[x][y] == idx + 1:
                    grid[r][c] = '#'
                    if backtrack(x, y,idx + 1):
                        return True
            return False
        return backtrack(0,0,0)