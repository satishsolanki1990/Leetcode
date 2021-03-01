'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''
'''
# with dictionary, 60 ms, faster than 45.19% o
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a={}
        self.count=0
        self.min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.count==0:
            self.min.append(x)            
        if x<=self.min[-1]:
            self.min.append(x)
        self.count+=1
        self.a[self.count]=x

    def pop(self):
        """
        :rtype: None
        """
        if self.min[-1]==self.a[self.count]:
            self.min.pop(-1)
        del self.a[self.count]
        self.count-=1
        

    def top(self):
        """
        :rtype: int
        """
        return self.a[self.count]

    def getMin(self):
        """
        :rtype: int
        """
        if self.count==1:
            return self.a[1]
        else:
            return self.min[-1]
'''

# with list,  52 ms, faster than 84.94%
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a=[]
        self.min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.a)==0:
            self.min.append(x)            
        if x<=self.min[-1]:
            self.min.append(x)
        self.a.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.min[-1]==self.a[-1]:
            self.min.pop(-1)
        self.a.pop(-1)
        
    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.a)==1:
            return self.a[0]
        else:
            return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
