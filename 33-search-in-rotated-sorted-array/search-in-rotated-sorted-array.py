class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # if nums[mid] < nums[right]: that means from mid to right is sorted
            # else: it is not sorted. 
            # note: if right side is not sorted, left side will. vise versa
            elif nums[mid] <= nums[right]: 
                # always look at the sorted side, if the sorted side contains target, search that side
                # else search the other side. 
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 

            else:
                if nums[left] <= target <= nums[mid]:
                    right =  mid - 1
                else:
                    left = mid + 1
        return -1

