class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(house_array):
            rob1, rob2 = 0, 0
            for n in house_array:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2


        return max(helper(nums[:-1]), helper(nums[1:]))
        
        