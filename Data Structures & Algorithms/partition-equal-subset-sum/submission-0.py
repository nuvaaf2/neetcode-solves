class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        total_sum = sum(nums)
        
        
        if total_sum % 2 != 0:
            return False
            
        
        target = total_sum // 2
        
       
        dp = set([0])
        
        
        for num in nums:
           
            next_dp = set()
            
            for current_sum in dp:
                
                next_dp.add(current_sum)
                
                
                next_dp.add(current_sum + num)
                
                
                if target in next_dp:
                    return True
                    
            
            dp = next_dp
            
        
        return False