'''
approach:
1. convert number to list of digits
2. look for the first 6:
3. conert it to 9
4. return the new number
corner: case: if there is no 6 in the number: return the number itself
'''


class Solution:
    def maximum69Number(self, num: int) -> int:
        num = [int(digit) for digit in str(num)]

        try:
            idx = num.index(6)
            num[idx] = 9
            num = [str(d) for d in num]
            num = int("".join(num))
            return num
        except:
            num = [str(d) for d in num]
            num = int("".join(num))
            return num
