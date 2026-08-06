class Solution:
    def subsetsWithDup(self, lst: list[int],  ans=None, i=0, lst1=None) -> list[list[int]]:
        if ans is None:
            ans = []
        if lst1 is None:
            lst1 = []
        if i == len(lst):
            if sorted(ans) not in lst1:
                lst1.append(sorted(ans.copy()))
            return lst1
        ans.append(lst[i])
        Solution().subsetsWithDup(lst, ans, i+1, lst1)
        ans.pop()
        Solution().subsetsWithDup(lst, ans, i+1, lst1)
        return lst1