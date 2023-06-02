'''
This approach can be improved. Mine beats only 10% of the submissions.
O(n^2)
'''

# from itertools import combinations
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pairs = combinations(nums,2)
#         for pair in pairs:
#             if sum(pair) == target:
#                 if len(set(pair)) ==1:
#                     return [i for i, x in enumerate(nums) if x == pair[0]]
#                 return [nums.index(pair[0]),nums.index(pair[1])]

'''
Approach 2: Using HashMap (beats 65% of the submissions)
O(n)
'''




from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap[target - nums[i]]]
            else:
                hashmap[nums[i]] = i
