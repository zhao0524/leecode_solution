class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # keep track of max distance, 
        # if the new max distance is > old, then we can return
        # current max distance is i + num[i] 
        max_range = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            curr_range = i + nums[i]
            if max_range > len(nums)-1 or i == len(nums) - 1 :
                return True
            if nums[i] == 0 and max_range == i:
                return False
            else:
                if max_range < curr_range:
                    max_range = curr_range

        return True
