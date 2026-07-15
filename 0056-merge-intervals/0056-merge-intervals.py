class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0] )
        lst = []
        for i in range(len(intervals)):
            if lst and intervals[i][0] <= lst[-1][1] :
                lst[-1][1] = max(intervals[i][1],lst[-1][1])
            else:
                lst.append(intervals[i])
        return lst
