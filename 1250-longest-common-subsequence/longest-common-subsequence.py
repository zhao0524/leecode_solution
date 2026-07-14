class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]

        for i in range(1, len(text2)+1):
            for j in range(1,len(text1)+1):
                if text1[j-1] == text2[i-1]:
                    m[i][j] = m[i-1][j-1] + 1
                else:
                    m[i][j] = max(m[i-1][j], m[i][j-1])
            
        return m[len(text2)][len(text1)]