class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if len(x) == 0:
            return True
        half = len(x) // 2
        for i in range(half):
            if x[i] != x[-(i+1)]:
                return False
        
        return True
                
        