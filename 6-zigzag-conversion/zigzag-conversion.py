class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(len(s) < numRows or numRows == 1 ):
            return s
        
        
        e = ""
        result = []
        b = 1
        k = 0
        final = ""
        for i in range(numRows):
            result.append(e)


        for i in s:
            result[k] = result[k]+i 

            k += b

            if(k == 0):
                b = 1
            elif k == numRows-1:
                b = -1
        
        for i in range(numRows):
            final += result[i]
        
        return final

        


