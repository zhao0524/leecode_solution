class Solution:
    def countAndSay(self, n: int) -> str:
        # force try
        last_RLE = "1"
        if n == 1:
            return "1"
        for _ in range(n-1):
            curr_count = 1
            RLE = ""
            for i in range(1,len(last_RLE)):
                if last_RLE[i] == last_RLE[i-1]:
                    curr_count += 1
                else:
                    RLE = RLE + str(curr_count) + last_RLE[i-1]
                    curr_count = 1
            RLE += str(curr_count) + last_RLE[-1]
            last_RLE = RLE

        return RLE
