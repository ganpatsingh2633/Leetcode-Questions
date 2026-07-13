class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def distinct(a,b,c,d):
            return a != b and a!=c and a!=d and b!=c and b!=d and c!=d
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    req = target - (nums[i] + nums[j] + nums[k])
                    if req in h and distinct(i,j,k, h[req]) :
                        x = tuple(sorted([nums[i], nums[j], nums[k], req]))
                        ans.add(x)
        return [ i for i in ans]
