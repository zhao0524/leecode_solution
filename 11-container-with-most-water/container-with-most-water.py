class Solution:
    def maxArea(self, height: list[int]) -> int:
        # loop from left and right, both pointer try to go to the middle. 
        l = 0
        r = len(height)-1
        max = 0
        while l < r:
            hl = height[l]
            hr = height[r]
            cur = (r - l) * min(hl, hr)
            if cur > max:
                max = cur
            
            if hl > hr:
                r = r - 1
            else:
                l = l + 1
        return max