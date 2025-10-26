class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return num
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if(nums[i] + nums[k] == target):
                    return [i,k]


        