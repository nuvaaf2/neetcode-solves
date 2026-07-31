class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i
            
        res = []
        size = 0
        end = 0
        
        
        for i, char in enumerate(s):
            size += 1
            
           
            end = max(end, last_index[char])
            
           
            if i == end:
                res.append(size)
                size = 0
                
        return res