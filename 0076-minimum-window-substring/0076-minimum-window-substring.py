from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t in s:
            return t
        if len(s) < len(t):
            return ""
        need = Counter(t)
        window = {}
        left = 0
        k = -1
        count = 0
        min1 = float('inf')
        for r , c in enumerate(s) :
            window[c] = window.get(c,0) + 1
            if c in need and need[c] >= window[c] :
                count += 1
            
            while count == len(t)  :
                if r - left + 1 < min1 :
                    min1 = r - left + 1
                    k = left
                xyx = s[left]
                window[xyx] -= 1
                if xyx in need and window[ xyx] < need[xyx]:
                    count -= 1
                left += 1
        return '' if k == -1 else s[k : k+min1]




# from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not s or not t or len(s) < len(t):
#             return ""
            
#         target_counts = Counter(t)
#         window_counts = Counter()
        
#         required_unique = len(target_counts)
#         satisfied_unique = 0
        
#         ans = (float('inf'), 0)
#         left = 0
        
#         for right, char in enumerate(s):
#             if char in target_counts:
#                 window_counts[char] += 1
#                 if window_counts[char] == target_counts[char]:
#                     satisfied_unique += 1
            
#             while satisfied_unique == required_unique:
#                 if right - left + 1 < ans[0]:
#                     ans = (right - left + 1, left)
                    
#                 left_char = s[left]
#                 if left_char in target_counts:
#                     if window_counts[left_char] == target_counts[left_char]:
#                         satisfied_unique -= 1
#                     window_counts[left_char] -= 1
                    
#                 left += 1
                
#         min_len, start_idx = ans
#         return "" if min_len == float('inf') else s[start_idx : start_idx + min_len]
