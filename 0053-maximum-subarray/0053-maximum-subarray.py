class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cur = 0
        for i in nums:
            cur += i
            if cur > maxsum:
                maxsum = cur
            if cur < 0 :
                cur = 0
        return maxsum




























        # current_sum=0
        # max_sum=nums[0]
        # for num in nums:
        #     current_sum+=num
        #     if current_sum>max_sum:
        #         max_sum=current_sum
        #     if current_sum<0:
        #         current_sum=0
        # return max_sum