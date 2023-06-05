'''
        Approach: Brute Force
        1. convert to set
        2. sort by descending order
        3. if len(sorted_list) is >=3 : return list[2]
        4. else : return max(list)
'''


class Solution:
    def thirdMax(self, nums: List[int]) -> int:    
        nums = list(set(nums))
        nums = sorted(nums, key=int, reverse=True)
        # print(nums)
        if len(nums) >= 3:
            return nums[2]
        else:
            return max(nums)
