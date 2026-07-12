class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return 
        x = nums[0]
        count = 1
        for i in nums:
            if i == x:
                count += 1
            else :
                count -= 1
            if count == 0:
                x = i
                count += 1
        return x
        # nums.sort()
        # if len(nums)%2 == 0:
        #     a = int(len(nums))
        #     b = a//2
        #     return nums[b]

        # else:
        #     a = int(len(nums))-1
        #     b = a//2
        #     return nums[b]