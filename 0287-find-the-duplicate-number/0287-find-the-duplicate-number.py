class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         seen =set()
#         for i in range(len(nums)):
#             if nums[i] in seen :
#                 return nums[i]
#             seen.add(nums[i])
        for i in range(len(nums)):
            idx = nums[i] if nums[i] >= 0 else nums[i] *(-1)
            if nums[idx] < 0 :
                return idx
            nums[idx] *= (-1)
