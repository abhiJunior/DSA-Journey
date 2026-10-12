class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0; h = 0 
        longest = float('-inf')
        hm = {}
        while (h < len(s)):
            if s[h] in hm:
                hm[s[h]] += 1
            else:
                hm[s[h]] = 1
            
            while h - l + 1 > len(hm):
                hm[s[l]] -= 1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l += 1

            if h - l + 1 == len(hm):
                longest = max(longest, h - l + 1)

            h += 1
        return longest

        