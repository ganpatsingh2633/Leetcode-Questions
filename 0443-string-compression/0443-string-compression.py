class Solution:
    def compress(self, s: List[str]) -> int:
        i = 0
        result = []
        while i < len(s):
            char = s[i]
            count = 0
            while i < len(s) and s[i] == char:
                count += 1
                i += 1
            result.append(char)
            if 10 > count > 1:
                result.append(str(count))
            elif count >= 10:
                n = []
                while count > 0:
                    n.append(str(count%10))
                    count //= 10
                result.extend(n[::-1])
        for i in range(len(result)):
            s[i] = result[i]
        del s[i+1:]
        return len(s)