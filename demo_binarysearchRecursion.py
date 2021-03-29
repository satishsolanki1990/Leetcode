'''
recursive binary search
'''

def binarysearch(arr,target):

    def helper(l,r):
        l = 0
        r = len(arr)
        mid= l + (r-l)//2
        if arr[mid] == target:
            return True
        elif arr[mid]>target:
            helper(mid+1,r)
        else:
            helper(l,mid-1)


