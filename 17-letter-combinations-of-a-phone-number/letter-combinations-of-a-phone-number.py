class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        for k in map[digits[0]]:
            result.append(k)

        for i in digits[1:]:
            temp = []
            for j in result:
                for k in map[i]:
                    temp.append(j+k)
            result = temp
        return result
