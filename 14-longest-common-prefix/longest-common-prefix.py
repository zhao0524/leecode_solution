class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0

        while i < len(strs[0]):
            c = strs[0][i]

            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return result

            result += c
            i += 1

        return result
