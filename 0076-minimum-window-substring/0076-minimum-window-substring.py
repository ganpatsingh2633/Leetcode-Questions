class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i in t:
            need[i] = need.get(i,0) + 1
        window = {}
        valid = 0
        l = r = 0
        start, length = 0 , float('inf')
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if r - l < length:
                    start = l
                    length = r - l
                d = s[l]
                l+=1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        if length == float('inf'):
            return ''
        return s[start:start+length]