class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        start, end = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                start, end = intervals[i]
                continue
            count += 1
            if intervals[i][1] < end:
                start, end = intervals[i]
                
            return count