class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        r = 0 
        c = len(matrix[0]) - 1 
        while c >= 0 and r <= len(matrix) - 1 :
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            elif target > matrix[r][c]:
                r += 1
        return False