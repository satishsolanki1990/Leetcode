# 1047. Remove All Adjacent Duplicates In String
"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

NOTE: only double of duplicate. Ex: 'abbaca' => 'ca' , 'abbbca' => 'abca'
"""

class Solution:
    def removeDuplicates(self, S):
        stack = []
        for i in range(len(S)):
            if len(stack) != 0:
                if stack[-1] != S[i]:
                    stack.append(S[i])
                else:
                    stack.pop(-1)
            else:
                stack.append(S[i])

        return ''.join(stack)


sol=Solution()
ip='abbaca'
print(sol.removeDuplicates(ip))