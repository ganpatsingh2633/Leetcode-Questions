class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1h = {}
        for i in s1:
            if i in s1h:
                s1h[i] +=1
                continue
            s1h[i] = 1
        s2h = {}
        for i in range(len(s2)):
            s2h[s2[i]] = s2h.get(s2[i], 0) + 1
            if i >= len(s1):
                l = s2[i - len(s1)]
                if s2h[l] == 1:
                    del s2h[l]
                else:
                    s2h[l] -= 1
            if s1h == s2h:
                return True
        return False