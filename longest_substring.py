'''
Logic:
2 pointers
sliding window
set theory
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l = l+1
            char_set.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen
