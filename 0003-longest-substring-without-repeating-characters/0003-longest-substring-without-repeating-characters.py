class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_value = 0
        distinct = []
        for i in range(len(s)):

            while s[i] in distinct:
                distinct.remove(distinct[0])

            distinct.append(s[i])
            max_value  = max(len(distinct),max_value)
        
        return max_value


        