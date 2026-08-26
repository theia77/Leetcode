class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        l=list(s)
        k=len(l)
        s=len(nums)
        k=1
        for i in range(1,s):
            
            if(nums[i]!=nums[i-1]):
                nums[k]=nums[i]
                k+=1
                
        return k
                
