class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for key in d.keys():
            if d[key]==1:
                L.append(key)
        return L