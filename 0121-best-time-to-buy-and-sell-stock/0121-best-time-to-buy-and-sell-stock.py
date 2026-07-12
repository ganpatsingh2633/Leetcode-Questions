class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = h = prices[0]
        res = 0
        for price in prices:
            if price < l:
                l = price
                h = price
            elif price > l:
                h = price
                res = max(res, h - l)
        return res






























        # low = high = prices[0]
        # res = 0
        # for price in prices :
        #     if price < low :
        #         low = price
        #         high = price
        #     elif price > high :
        #         high = price
        #         res = max(res , high - low)
        # return res