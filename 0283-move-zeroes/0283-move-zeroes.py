class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        k = len(nums) - 1
        while i <= k:
            if i < k and nums[i] == 0:
                j = i
                while j < k :
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j += 1
                k -= 1
                i = i + (0 if nums[i] == 0 else 1)
            else:
                i+=1