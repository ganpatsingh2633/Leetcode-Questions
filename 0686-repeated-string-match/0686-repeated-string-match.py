class Solution:
    def repeatedStringMatch(self, s1: str, s2: str) -> int:
        x = ''
        c = 0
        while s2 not in x:
            x += s1
            c += 1
            if c > (len(s2) // len(s1)) + 2:
                return -1
        return c