class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [i + 1 for i in range(n)]
        k = k - 1
        res = []
        def fact(n):
            if n == 1 :
                return 1
            return n * fact(n -1)
        for _ in range(n ):
            if len(lst) == 1:
                res.append(lst[0])
                break
            b = fact(len(lst) - 1)
            idx = k // b
            res.append(lst[idx])
            del lst[idx]
            k = k % b
        
        return ''.join([str(i) for i in res])