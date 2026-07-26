class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l,r = 0, len(height) - 1
        Lmax = Rmax = 0
        while l < r :
            if height[l] < height[r]:
                Lmax = max(Lmax, height[l])
                ans += Lmax - height[l]
                l+=1
            else:
                Rmax = max(Rmax, height[r])
                ans += Rmax - height[r]
                r -= 1
        return ans