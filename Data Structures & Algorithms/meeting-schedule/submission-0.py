class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        
        if not intervals:
            return True

        
        intervals.sort(key=lambda i: i.start)

        
        for i in range(1, len(intervals)):
            
            
            prev_end = intervals[i - 1].end
            
           
            curr_start = intervals[i].start

           
            if curr_start < prev_end:
                return False

       
        return True
    