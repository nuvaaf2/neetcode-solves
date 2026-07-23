class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
            
       
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res = 0
        count = 0
        s, e = 0, 0
        
        
        while s < len(intervals):
            
            
            if start[s] < end[e]:
                s += 1
                count += 1
                
            
            else:
                e += 1
                count -= 1
                
           
            res = max(res, count)
            
        return res