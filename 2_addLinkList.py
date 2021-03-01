'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # add one by one and save digit reminder of 10
        l=[]
        print(l1)
        carry_forward=0
        while (True):
            if (l1.val != None) and (l2.val!= None) :
                temp=(l1.val+l2.val)
                if (temp+carry_forward)<10:
                    l.append(temp+carry_forward)
                    carry_forward=0
                else:
                    l.append((temp+carry_forward)%10)
                    carry_forward=1
            if (l1.next == None) or (l2.next == None):
                if (l1.next == l2.next):
                    if carry_forward ==1:
                        l.append(1)
                    break
                else:
                    if (l2.next != None): 
                        l2=l2.next
                        l1.val=None
                        temp=l2.val+carry_forward
                        if temp<10:
                            l.append(temp)
                            carry_forward=0
                        else:
                            l.append(temp%10)
                            carry_forward=1
                    else:  
                        l1=l1.next
                        l2.val=None
                        temp=l1.val+carry_forward
                        if temp<10:
                            l.append(temp)
                            carry_forward=0
                        else:
                            l.append(temp%10)
                            carry_forward=1
            else:
                l1=l1.next
                l2=l2.next
        print(l)
        return List2LinkList(l)
            
def List2LinkList(l):
    if len(l)==1:
        return ListNode(l[0])
    L=ListNode(l[0],List2LinkList(l[1:]))
    return L
