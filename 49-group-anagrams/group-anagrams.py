class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sample = {}
        result = []
        count = 0
        for i in strs:
            s = "".join(sorted(i))
            
            if s in sample:
                # find the correct index(count) and store at that list
                index = sample[s]
                result[index].append(i)

            else:
                result.append([i])
                sample[s] = count
                count += 1

        return result
        


