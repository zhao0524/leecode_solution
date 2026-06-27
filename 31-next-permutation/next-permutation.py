class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        if len(nums) == 2:
            t = nums[0]
            nums[0] = nums[1]
            nums[1] = t
            return

        pivot = -1

        # Find pivot
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break

        # If no pivot exists, nums is fully decreasing
        if pivot == -1:
            nums.sort()
            return

        # Find the smallest number greater than nums[pivot]
        min_index = pivot + 1

        for j in range(pivot + 1, len(nums)):
            if nums[j] > nums[pivot] and nums[j] <= nums[min_index]:
                min_index = j

        # Swap nums[pivot] with nums[min_index]
        nums[pivot], nums[min_index] = nums[min_index], nums[pivot]

        # Sort everything after pivot
        nums[pivot + 1:] = sorted(nums[pivot + 1:])

                