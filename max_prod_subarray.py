'''
Approach: Dynamic Programming
Corner case: if encountered 0
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMin, curMax = 1, 1
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * num
            curMax = max(num, num * curMin, num * curMax)
            curMin = min(num, num * curMin, temp)

            ans = max(ans, curMax)
        return ans
