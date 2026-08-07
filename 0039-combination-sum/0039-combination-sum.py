# class Solution:
#     def combinationSum(self, candidates: List[int], target: int, sum1 = 0, j = 0, ans = None, lst1 = None) -> List[List[int]]:
#         if ans is None:
#             ans = []
#         if lst1 is None:
#             lst1 = []
#         if sum1 == target:
#             if sorted(ans) not in lst1:
#                 lst1.append(sorted(ans.copy()))
#             return lst1
#         if sum1 > target:
#             return lst1
#         for i in range(j, len(candidates)):
#             ans.append(candidates[i])
#             Solution().combinationSum(candidates,target,sum1 + candidates[i], i, ans,lst1)
#             ans.pop()
#         return lst1


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         result = []
#         candidates.sort() # Optional: Sorting can help with pruning but not strictly necessary for correctness
# here.
#         def backtrack(current_sum, start_index, current_combination):
#             if current_sum == target:
#                 result.append(list(current_combination))
#                 return
#             if current_sum > target:
#                 return
#             for i in range(start_index, len(candidates)):
#                 # Optimization: if current_sum + candidates[i] > target, no need to proceed with larger numbers
#                 # This requires candidates to be sorted.
#                 if current_sum + candidates[i] > target:
#                     break 
#                 current_combination.append(candidates[i])
#                 backtrack(current_sum + candidates[i], i, current_combination)
#                 current_combination.pop()
#         backtrack(0, 0, [])
#         return result


class Solution: 
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        lst1 = []
        def backtrack(sum1, j, ans):
            if sum1 == target:
                lst1.append(sorted(ans.copy()))
                return 
            if sum1 > target:
                return
            for i in range(j, len(candidates)):
                if sum1 + candidates[i] > target:
                    break
                ans.append(candidates[i])
                backtrack(sum1 + candidates[i], i, ans)
                ans.pop()
        backtrack(0,0,[])
        return lst1