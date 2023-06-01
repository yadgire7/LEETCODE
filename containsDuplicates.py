from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        product = 1
        cnt = Counter(nums)
        print(cnt)
        print(cnt.values())
        i = iter(cnt.values())
        product = product*next(i)
        print(product)
        if product != 1:
            return "true"
        else:
            return "false"
