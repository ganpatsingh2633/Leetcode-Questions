class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l , r = 1 , max(quantities)
        def num1(m):
            return sum((q-1)//m+1 for q in quantities)
        while l < r :
            m = (l + r)//2
            if num1(m) <= n:
                r = m
            else :
                l = m + 1 
        return l
        # sum1  = 0
        # for i in quantities:
        #     sum1 += i
        # if sum1 % n == 0 :
        #     return sum1 // n
        # else :
        #     return (sum1 // n) + 1