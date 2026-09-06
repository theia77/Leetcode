class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=[]
        b=[]
        final=[]
        if(k>len(nums)):
            k=k%len(nums)
        a=nums[:len(nums)-k]
        b=nums[len(nums)-k:]
        final=b+a
        nums[:]=final

            
        