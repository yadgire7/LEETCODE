'''
Problem Number: 1913
Logic:
1. sort the list
2. choose first 2 elements as pair 1
3. choose last two elements as pair 2
4. return product(pair 1) - product(pair 2)
'''

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        N = len(nums)
        w, x = nums[N-1], nums[N-2]
        y, z = nums[0], nums[1]
        return (w*x) - (y*z)