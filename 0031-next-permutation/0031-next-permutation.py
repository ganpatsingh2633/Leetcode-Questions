class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = -1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                p = i
        if p == -1 :
            i = 0
            j  = len(nums) -1
            while i <= j:
                nums[i] , nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        else :
            m = float('inf')
            k = -1
            for i in range(p+1,len(nums)):
                if nums[i] <= m and nums[i] > nums[p] :
                    m = nums[i]
                    k = i
            if k!= -1:
                nums[k],nums[p] = nums[p] , nums[k]
            i = p +1 
            j  = len(nums) -1
            while i <= j:
                nums[i] , nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums