class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        i = 0
        j = len(x) -1
        while i < j:
            x[i],x[j] = x[j], x[i]
            i+=1
            j -=1
        return ' '.join(x)