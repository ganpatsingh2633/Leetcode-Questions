class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2) 
        i = j = 0
        arr = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i +=1
            else:
                arr.append(nums2[j])
                j+=1
        while i < n :
            arr.append(nums1[i])
            i+=1
        while j < m :
            arr.append(nums2[j])
            j += 1
        if len(arr) % 2 == 0:
            m = (len(arr) -1) // 2
            return ( arr[m]  + arr[m+1] ) / 2
        else : return arr[(len(arr) - 1 )// 2]