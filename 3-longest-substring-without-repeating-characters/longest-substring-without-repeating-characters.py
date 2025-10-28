class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_string = ""
        longest_string = ""
        for i in range(len(s)):
            ch = s[i]
            if ch in curr_string:
                prev = curr_string.index(ch)
                curr_string = curr_string[prev + 1:]

            curr_string = curr_string + s[i]
            
            if len(curr_string) > len(longest_string):
                    longest_string = curr_string
            print(longest_string)


        return len(longest_string)

        

        