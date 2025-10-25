class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.pref = [0]
        s = 0
        for x in nums:
            s += x
            self.pref.append(s)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.pref[right + 1] - self.pref[left]