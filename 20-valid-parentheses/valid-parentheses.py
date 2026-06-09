class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 != 0):
            return False
        st = ""
        left = "([{"
        right = ")]}"
        for i in s:
            if(i in left):
                st += i
            else:
                if(len(st) == 0 or st[-1] != left[right.index(i)]):
                    return False
                else:
                    st = st[0:-1]
        if len(st) == 0:
            return True
        else:
            return False