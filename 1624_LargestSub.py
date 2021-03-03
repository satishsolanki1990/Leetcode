class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        max_sub = -1
        # convert into dict
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = i
            else:
                max_sub = max(max_sub, i - d[ch] - 1)

        return max_sub

sol = Solution()
s = "cabbac"
print(sol.maxLengthBetweenEqualCharacters(s))