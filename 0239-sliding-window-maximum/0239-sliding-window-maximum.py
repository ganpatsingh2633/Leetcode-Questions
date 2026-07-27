from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans= []
        q = deque()
        for i, cur in enumerate(nums):
            while q and cur >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
            if len(q) >= k or i-k + 1 >= q[0]:
                q.popleft()
        return ans


# from collections import deque
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         ans= []
#         q = deque()
#         smax = max1 = float('-inf')
#         for i in nums:
#             q.append(i)
#             if i > max1:
#                 smax = max1
#                 max1 = i
#             elif i > smax and i < max1:
#                 smax = i
#             if len(q) == k:
#                 ans.append(max1)
#                 a = q.popleft()
#                 if a == max1:
#                     max1 = smax
#         return ans

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k > len(nums):
#             return        
#         i = 0 
#         j = i + k - 1
#         arr = []
#         max1 = float('-inf')
#         while j < len(nums):
#             if i > j:
#                 arr.append(max1)
#                 j = i
#                 i = j-k + 1
#                 max1 = float('-inf')
#                 continue
#             max1 = max(max1, nums[i])
#             i+=1
#         return arr