# class Solution:
#     def compress(self, s: List[str]) -> int:
#         i = 0
#         k = 0
#         while i < len(s):
#             char = s[i]
#             count = 0
#             while i < len(s) and s[i] == char:
#                 count += 1
#                 i += 1
#             s[k] = char
#             k+=1
#             if 10 > count > 1:
#                 s[k] = str(count)
#                 k+=1
#             elif count >= 10:
#                 n = []
#                 while count > 0:
#                     n.append(str(count%10))
#                     count //= 10
#                 for ch in n[::-1]:
#                     s[k] = str(ch)
#                     k +=1
#         del s[k:]
#         return len(s)
class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0
        while i < len(chars):
            j = i+1

            while j<len(chars) and chars[j] == chars[i]:
                j += 1
            
            leng = j-i
            if leng>1:
                chars[i:j] = chars[i]+str(leng)
                i += 1 + len(str(leng))
            else:
                i +=1
        
        return len(chars)
        