class Solution:
    def binaryGap(self, N: int) -> int:
        count = 0
        max_count = 0
        found = False
        while N>0:
            c = N%2
            N = N//2
            if c == 0 and found:
                count += 1
            elif c == 1:
                found = True
                max_count = max(count, max_count)
                count = 1
        return max_count