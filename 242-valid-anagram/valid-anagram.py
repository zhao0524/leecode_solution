class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in hash_s:
                hash_s[i] += 1
            else:
                hash_s[i] = 1
        
        for i in t:
            if i in hash_s:
                if hash_s[i] == 0:
                    return False
                else:
                    hash_s[i] -= 1
            else:
                return False

        return True 
        

        