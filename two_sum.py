'''
This approach can be improved. Mine beats only 10% of the submissions.
'''

from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = combinations(nums,2)
        for pair in pairs:
            if sum(pair) == target:
                if len(set(pair)) ==1:
                    return [i for i, x in enumerate(nums) if x == pair[0]]
                return [nums.index(pair[0]),nums.index(pair[1])]