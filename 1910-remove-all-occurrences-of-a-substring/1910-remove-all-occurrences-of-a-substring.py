# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         stack = []
#         m = len(part)
#         for i in s:
#             stack.append(i)
#             if len(stack) >= m and ''.join([x for x in stack[-m :]]) in part:
#                 del stack[-m :]
#         return ''.join(stack)


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part,"",1)
        return s
