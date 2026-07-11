class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = 0
        j = 0
        arr = []
        while i < m or j < n :
            if j == n :
                arr.append(nums1[i])
                i+=1
            elif i == m :
                arr.append(nums2[j])
                j+=1
            elif nums1[i] < nums2[j] :
                arr.append(nums1[i])
                i+=1
            else :
                arr.append(nums2[j])
                j+=1
        for i in range(n+m):
            nums1[i] = arr[i]