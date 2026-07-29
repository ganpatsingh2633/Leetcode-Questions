class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)
        for i in s:
            stack.append(i)
            if len(stack) >= m and ''.join([x for x in stack[-m :]]) in part:
                del stack[-m :]
            # if len(stack) == 0:
            #     return ''
        return ''.join(stack)