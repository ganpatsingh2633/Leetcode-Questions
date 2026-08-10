class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,m,r):
            i =  l
            j = m + 1
            k  = l
            lst = []
            while i <= m and j <= r:
                if nums[i] < nums[j]:
                    lst.append(nums[i])
                    i += 1
                else : 
                    lst.append(nums[j])
                    j += 1
            while i <= m :
                lst.append(nums[i])
                i += 1
            while j <= r :
                lst.append(nums[j])
                j+=1
            for i in range(len(lst)):
                nums[k] = lst[i]
                k+=1
        def divide(l,r):
            if l>=r :
                return
            m = (l+r)//2
            divide(l,m)
            divide(m+1, r)
            merge(l,m,r)
        divide(0,len(nums) -1 )
        return nums