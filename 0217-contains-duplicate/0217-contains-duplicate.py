class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        if(max(d.values())!=1):
            return True
        else:
            return False