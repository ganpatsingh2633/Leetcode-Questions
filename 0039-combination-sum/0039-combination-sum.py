class Solution:
    def combinationSum(self, candidates: List[int], target: int, sum1 = 0, j = 0, ans = None, lst1 = None) -> List[List[int]]:
        if ans is None:
            ans = []
        if lst1 is None:
            lst1 = []
        if sum1 == target:
            if sorted(ans) not in lst1:
                lst1.append(sorted(ans.copy()))
            return lst1
        if sum1 > target:
            return lst1
        for i in range(j, len(candidates)):
            ans.append(candidates[i])
            Solution().combinationSum(candidates,target,sum1 + candidates[i], i, ans,lst1)
            ans.pop()
        return lst1




















    # # Inner recursive function uses structural parameters instead of loops or external side effects
    #     def recurse(index: int, rem_target: int) -> list[list[int]]:
    #         # Base case 1: Target reached exactly
    #         if rem_target == 0:
    #             return [[]]
            
    #         # Base case 2: Target exceeded or out of candidates bounds
    #         if rem_target < 0 or index == len(candidates):
    #             return []
            
    #         # Choice 1: Pick the current element (keep index the same to allow reuse)
    #         pick_combinations = recurse(index, rem_target - candidates[index])
    #         # Append the picked element to the front of all sub-results
    #         picked_results = [[candidates[index]] + combo for combo in pick_combinations]
            
    #         # Choice 2: Skip the current element (move to the next index)
    #         skip_results = recurse(index + 1, rem_target)
            
    #         # Combine structural results
    #         return picked_results + skip_results
    #     return recurse(0, target)