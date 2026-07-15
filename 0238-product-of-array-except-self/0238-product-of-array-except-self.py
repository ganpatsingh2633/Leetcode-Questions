# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         r = [0] * len(nums)
#         l = [0] * len(nums)
#         r[-1] = 1
#         l[0] = 1
#         ans = []
#         for i in range(len(nums)-2,-1,-1):
#             r[i] = r[i+1] * nums[i+1]
#         for i in range(1 ,len(nums)):
#             l[i] = l[i-1] * nums[i-1]
#         for i in range(len(nums)):
#             ans.append(r[i] * l[i])
#         return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        n_zero = 0
        for num in nums:
            product_all *= num
            if num == 0:
                n_zero += 1
        if n_zero == 0:
            return [product_all//num for num in nums]
        if n_zero == 1:
            product_without_zero = 1
            for num in nums:
                if num != 0:
                    product_without_zero *= num
            return [0 if num != 0 else product_without_zero for num in nums]
        if n_zero > 1:
            return [0 for num in nums]