class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = {0:1}
        cur = 0
        c = 0
        for i in range(len(nums)):
            cur += nums[i]
            if cur - k in h :
                c += h[cur - k]
            if cur in h :
                h[cur] += 1
            else:
                h[cur] = 1
        return c