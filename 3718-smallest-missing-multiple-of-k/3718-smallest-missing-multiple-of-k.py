class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=list(set(nums))
        d={}
        for i in range(len(nums)):
            if nums[i]%k==0:
                key=nums[i]//k
                value=nums[i]
                d[key]=value
        num=set(d.keys())
        i=1
        while True:
            if i not in num:
                return i*k
                break
            else: 
                i=i+1