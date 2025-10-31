class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        new = []
        if x < 0:
            neg = True
            x = -(x)
        x = str(x)

        for i in x:
            new.insert(0,i)

        for i in new:
            if new[0] == 0:
                new.pop(0)

        final = int(''.join(new))
        if neg:
            final = -final
        return final if -2**31 <= final <= 2**31 - 1 else 0
        

        

        