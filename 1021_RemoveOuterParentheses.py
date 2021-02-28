"""
Given a valid parentheses string S, consider its primitive decomposition:
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string
in the primitive decomposition of S.

Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""


class Solution:
    def removeOuterParentheses(self, S):
        '''
        logic: remove first parenthesis '(' and find its complementary')'
        remove next and so on.

        to do that, use stack and pointer.
        '''

        stack = []

        l = 0
        r = 0
        res = ''
        for i in S:
            r += 1
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
            if len(stack) == 0:
                res += S[l + 1:r - 1]
                l = r

        return res


sol=Solution()

S="(()())(())"

print(sol.removeOuterParentheses(S))