'''
Approach 1: 
1. Converst string to list
2. sort the list
3. if equal: return true; else: return false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t
