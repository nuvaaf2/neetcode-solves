from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_window = Counter(s2[:len(s1)])
        left = 0
        
        if count_s1 == count_window:
            return True
        
        for right in range(len(s1), len(s2)):
            count_window[s2[right]] += 1
            
            count_window[s2[left]] -= 1
            if count_window[s2[left]] == 0:
                del count_window[s2[left]]
            left += 1
            
            if count_s1 == count_window:
                return True
        
        return False