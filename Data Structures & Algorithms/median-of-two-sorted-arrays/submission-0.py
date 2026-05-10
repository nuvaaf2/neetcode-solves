class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(nums1)

        while True:
            i = (l + r) // 2
            j = half - i
            
            num1left = nums1[i-1] if i > 0 else float("-infinity")
            num1right = nums1[i] if i < len(nums1) else float("infinity")
            num2left = nums2[j-1] if j > 0 else float("-infinity")
            num2right = nums2[j] if j < len(nums2) else float("infinity")
            
            if num1left <= num2right and num2left <= num1right:
                
                if total % 2 != 0: 
                    
                    return min(num1right, num2right)
                else: 
                   
                    return (max(num1left, num2left) + min(num1right, num2right)) / 2.0
                    
            elif num1left > num2right:
                r = i - 1
            else:
                l = i + 1