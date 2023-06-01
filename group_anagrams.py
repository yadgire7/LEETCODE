'''
logic: characters in similar words are same, so we can sort the characters and use it as a key to store the words in a dictionary
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for s in strs:
            key = str(sorted([*s]))
            if key not in myDict.keys():
                myDict[key] = [s]
            else:
                myDict[key].append(s)

        return list(myDict.values())
