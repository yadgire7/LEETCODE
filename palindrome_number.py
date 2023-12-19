'''
Using 2 pointers
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            divisor = 1

            while x >= 10 * divisor:
                divisor = divisor * 10

            while x:
                right = x % 10
                left = x // divisor
                if left != right:
                    return False
                else:
                    x = (x % divisor) // 10
                    divisor = divisor / 100
            return True
