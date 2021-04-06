'''
recursive binary search
'''

def binarysearch(arr,target):

    mid = 0
    def helper(l,r):
        if l>r:
            return -1
        nonlocal mid, target
        mid= l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            return helper(l,mid-1)
        else:
            return helper(mid+1,r)

    return helper(0, len(arr))

arr= [1,2,4,5,7,8,9]
target=4

print(binarysearch(arr,target))

