class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in strs:
            x = ''.join(sorted(i))
            if x not in h.keys() :
                h[x] = [i]
            else :
                h[x].append(i)
        return [ v for v in h.values()]