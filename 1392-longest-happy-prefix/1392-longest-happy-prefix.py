class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(len(s)):
            if s[:-i] == s[i:]:
                return s[:-i]
        return ''