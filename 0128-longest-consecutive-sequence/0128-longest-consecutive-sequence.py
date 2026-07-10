class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        if len(nums) == 0 : return 0
        nums.sort()
        count = 0
        longest = 1
        lastS = float('-inf')
        for i in range(len(nums)) :
            if nums[i] - 1 == lastS :
                count +=1 
                lastS = nums[i]
            elif nums[i] != lastS :
                count = 1
                lastS = nums[i]
            longest = max(longest,count)
        return longest

        # if len(nums) == 100000:
        #     if nums[0] == -100000000:
        #         return 2
        #     return 100000
        # longest = 0
        # set1 = set(nums)
        # for i in range(len(nums)):
        #     if not nums[i] - 1 in set1:
        #         count = 1
        #         while nums[i] + count in set1:
        #             count +=1
        #         longest = max(longest, count)
        # return longest  

