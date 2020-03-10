class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        # method :1, Brute force method
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    return [i,j]
        """
# method :2, divide and conqure
        if len(nums)==2:
            return [0,1]
        
        try:
            l=[i for i in range(len(nums)) if nums[i] == (target/2) ]
            print(l)
            if len(l)==2:
                return l
        except ValueError:
            print('continue')        
                
        nums0=sorted(nums)
        l=[]
        flag1=len(nums)
        if nums0[0]> 0:
            for i in range(len(nums0)):
                if nums0[i]>=target:
                    flag1=i
                    break        
        # take the list only till flag1
        nums1=nums0[0:flag1]
        # make flag2 as nums1[] < target
        
        for i in range(len(nums1)):
            if nums1[i]>target/2:
                flag2=i
                break
        # Two for loops
        for i in range(flag2):
            for j in range(flag2,flag1):
                if nums1[i]+nums1[j]==target:
                    return [nums.index(nums1[i]),nums.index(nums1[j])]
                    break                    
        return l
    
    # find index for a number < (target/2)
    # use that as flag1 and split the list
    # if nums has all positive numbers the maximum index it will go till target
