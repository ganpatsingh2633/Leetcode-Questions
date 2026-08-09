class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        def backtrack(idx, path):
            if idx == len(nums):
                results.append(path.copy())
                return 
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0,[])
        return results