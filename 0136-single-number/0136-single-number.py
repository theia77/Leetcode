class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for s in d:
            if(d[s]==1):
                return s