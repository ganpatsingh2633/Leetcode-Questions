class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i -1] == nums[i] : continue
            j , k = i+1 , len(nums) - 1
            while j < k :
                sum1 = nums[i] + nums[j] + nums[k]
                if sum1 == 0:
                    ans.append([nums[i] , nums[j] , nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j] : j+=1
                    while j<k and nums[k+1] == nums[k] : k -= 1
                elif sum1 < 0 : j+=1
                else : k-=1
        return ans