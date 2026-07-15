class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [0] * len(nums)
        l = [0] * len(nums)
        r[-1] = 1
        l[0] = 1
        ans = []
        for i in range(len(nums)-2,-1,-1):
            r[i] = r[i+1] * nums[i+1]
        for i in range(1 ,len(nums)):
            l[i] = l[i-1] * nums[i-1]
        for i in range(len(nums)):
            ans.append(r[i] * l[i])
        return ans