# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row = -1
        # for i in range(len(matrix)) :
        #     if target >= matrix[i][0] and target <= matrix[i][-1]:
        #         row = i
        # for i in range(len(matrix[row])):
        #     if matrix[row][i] == target:
        #         return True
        # return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i , j = 0 , (rows * cols) -1
        while i <= j :
            mid = (i + j) // 2
            row  = mid // cols
            col = mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                i = mid + 1
            else : 
                j = mid - 1
        return False