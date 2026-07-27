class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = [0] * n
        r = [0] * n
        s = []
        for i in range(len(heights)):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            l[i] = s[-1] if s else -1
            s.append(i)  
        s = []
        maxarea = 0
        for i in range(n-1, -1 , -1):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            r[i] = s[-1] if s else n
            maxarea = max(maxarea, (r[i] - l[i] - 1) * heights[i])
            s.append(i)
        return maxarea




# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxarea = 0
#         for i in range(len(heights)):
#             minh = heights[i]
#             l = r = i
#             while l > 0 and heights[l - 1 ] >= minh:
#                 l -= 1
#             while r < len(heights) - 1 and heights[r + 1] >= minh:
#                 r +=1
#             maxarea = max(maxarea, minh * (r - l + 1) )
#         return maxarea