'''
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.



Example 1:

Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.

'''


class Solution:
    def isArmstrong(self, n: int) -> bool:
        return n == sum([int(v) ** len(str(n)) for v in str(n)])  # this is most fastest
# METHOD -1
#         k = math.floor(math.log10(n)) + 1
#         c = n
#         while c: # Terminates when c is 0
#             digit = c % 10 # Extract the digit
#             total += digit ** k
#             c //= 10
#         return total == n

# METHOD -2
#         digits = len(str(n))
#         arm=0
#         original=n
#         for i in range(digits-1,-1,-1):
#             arm += (n//(10**i))**digits
#             n %= (10**i)

#         return arm ==  original