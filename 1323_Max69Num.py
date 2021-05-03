'''
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



Example 1:

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

'''


class Solution:
    def maximum69Number(self, num: int) -> int:
        l = list(str(num))
        for i in range(len(l)):
            if l[i] == '6':
                l[i] = '9'
                break

        return int(''.join(l))

#         ans=0
#         n=len(str(num))
#         flag=True
#         for i in range(n-1,-1,-1):
#             digit = num//(10**i)
#             if  flag == True and digit== 6:
#                 flag=False
#                 ans += (9*(10**i))
#             else:
#                 ans += (digit*(10**i))

#             num %=(10**i)

#         return ans
# #ANOTHER METHOD:
#         return int(str(num).replace('6', '9', 1))
