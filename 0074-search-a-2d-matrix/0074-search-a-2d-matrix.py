class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for i in range(len(matrix)) :
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                row = i
        for i in range(len(matrix[row])):
            if matrix[row][i] == target:
                return True
        return False