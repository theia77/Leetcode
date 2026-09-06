class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[]
        right=[]
        prod=1
        for i in range(len(nums)):
            left.append(prod)
            prod*=nums[i]
        prod1=1
        for k in range(len(nums)-1,-1,-1):
            right.append(prod1)
            prod1*=nums[k]
        right.reverse()
        L=[]
        for j in range(len(nums)):
            L.append(left[j]*right[j])
        return L