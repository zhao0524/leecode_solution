class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0 
        right = len(nums) - 1 
        left_target = -1 
        right_target = -1 

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # action
                left_target = mid
                right = mid - 1 

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 
        left = 0 
        right = len(nums) - 1 
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # action
                right_target = mid
                left = mid + 1 
                
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 

        return [left_target, right_target]
            
        
        
        