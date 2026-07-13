class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                seen =set()
                for k in range(j+1,len(nums)):
                    req = target - (nums[i] + nums[j] + nums[k])
                    if req in seen :
                        x = tuple(sorted([nums[i], nums[j], nums[k], req]))
                        ans.add(x)
                    seen.add(nums[k])
        return [ i for i in ans]