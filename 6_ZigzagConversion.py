"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on
a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # another method using pattern (better than 40.91%)
        s1=''
        n=numRows
        if n==1:
            return s

        k=0
        for i in range(n):
            j=i
            flag=0
            if i==0 or i==(n-1):
                k=0
            while True:
                try:
                    if k==0:
                        s1+=s[j]
                        j+=(2*(n-1) - k)
                    else:
                        if flag==0:
                            s1+=s[j]
                            j+=(2*(n-1) - k)
                            flag=1
                        else:
                            s1+=s[j]
                            j+=k
                            flag=0
                except:
                    break
            k+=2
            
        return s1
                
"""
# Method 1: brute force method (11.69%)
        c=1
        n=numRows
        if n==1:
            return s
        dic=CreateDict(n)
        j=0
        for i in range(len(s)): 
            
            dic[j].append(s[i])
            if j==0:
                c=1
            if j==n-1:
                c=-1
            j+=c 
        return JoinAll(dic,n)
"""                

"""
def CreateDict(n):
    dic={}
    for i in range(n):
        dic[i]=[]
    return dic
    
def JoinAll(dic,n):
    s=''
    for i in range(n):
        temp=''.join(dic[i])
        s+=temp
    return s
    
"""
