'''
It is used to reduce search space by half.
most of time, if sorted array or data is given
time complexity = O(log(n))

for ex: search a number from sorted list
'''
def binarySearch(arr,target):
    l=0
    r=len(arr)
    while(l<=r):
        mid = l+(r-l)//2
        if arr[mid] == target:
            print(f'target {target} found at index {mid} or position {mid+1}  in array.')
            return True

        if arr[mid]>target:
            r=mid-1
        else:
            l = mid +1

    print(f'target {target} not found in array.')
    return False

a=[1,2,4,5,6,8]
binarySearch(a,1)


