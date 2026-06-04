class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(len(s) < numRows or numRows == 1 ):
            return s
        
        
        result = [""] * numRows
        b = 1
        k = 0

        for i in s:
            result[k] = result[k]+i 

            k += b

            if(k == 0):
                b = 1
            elif k == numRows-1:
                b = -1
        
        return "".join(result)

        


