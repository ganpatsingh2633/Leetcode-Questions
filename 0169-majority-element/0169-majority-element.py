class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2 == 0:
            a = int(len(nums))
            b = a//2
            return nums[b]

        else:
            a = int(len(nums))-1
            b = a//2
            return nums[b]