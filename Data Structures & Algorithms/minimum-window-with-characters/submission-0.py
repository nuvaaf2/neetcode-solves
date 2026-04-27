from collections import Counter
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)
        window = {}
        
        have = 0
        required = len(need)
        
        left = 0
        result = float("inf"), 0, 0
        
        for right in range(len(s)):
            char = s[right]
            
            # Add char to window
            window[char] = window.get(char, 0) + 1
            
            # Check if satisfied
            if char in need and window[char] == need[char]:
                have += 1
            
            # Shrink from left
            while have == required:
                if (right - left + 1) < result[0]:
                    result = (right - left + 1, left, right)
                
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        
        length, l, r = result
        return s[l : r + 1] if length != float("inf") else ""