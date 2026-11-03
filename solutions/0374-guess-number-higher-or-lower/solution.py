# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:
            my_guess = (left + right) // 2

            res = guess(my_guess)

            if res == -1:
                right = my_guess - 1
            
            elif res == 1:
                left = my_guess + 1

            else:
                return my_guess

