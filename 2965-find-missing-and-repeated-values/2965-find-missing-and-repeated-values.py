class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        h = {}
        m = None
        f = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in h:
                    f = grid[i][j] 
                h[grid[i][j]] = 1 
        for i in range(1 , (len(grid) * len(grid)) + 1):
            if i not in h :
                m = i
                break
        return [f,m]
            