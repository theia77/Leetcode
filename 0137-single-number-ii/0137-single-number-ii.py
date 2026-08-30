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
        for key in d.keys():
            if d[key]==1:
                return key