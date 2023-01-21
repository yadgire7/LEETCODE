class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        cnt = {k: 0 for k in nums_set}
        for n in nums:
            cnt[n] += 1
        return (min(cnt, key=cnt.get))
