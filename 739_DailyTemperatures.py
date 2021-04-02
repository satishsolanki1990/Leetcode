'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures
T = [73, 74, 75, 71, 69, 72, 76, 73],

your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

'''
T = [73, 74, 75, 71, 69, 72, 76, 73]

class SolutionON:
    def dailyTemperatures(self, T):
        result, stack = [0] * len(T), []
        # stack.append((T[0],0))
        for index, val in enumerate(T):
            # index+=1
            while stack and val > stack[-1][0]:
                result[stack[-1][1]] = (index - stack[-1][1])
                stack.pop()
            stack.append((val, index))

        return result

# class Solution:
#     def dailyTemperatures(self, T):
#         curr=0
#         next_=curr+1
#         n=len(T)
#         ans=[]
#         while(curr<n):
#           while(next_< n and T[next_]<=T[curr]): next_ +=1
#           if next_ < n-1:
#             ans.append(next_-curr)
#           else:
#             ans.append(0)
#           curr+=1
#           next_ = curr+1
#         return ans

# T=[73, 74, 75]
T = [73, 74, 75, 71, 69, 72, 76, 73]

# s=Solution()
s = SolutionON()
print(s.dailyTemperatures(T))


