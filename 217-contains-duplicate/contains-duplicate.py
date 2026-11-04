class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {} 

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen[nums[i]] = 1
        return False

