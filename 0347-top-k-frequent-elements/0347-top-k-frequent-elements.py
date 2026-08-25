class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        d=sorted(d.items(), key=lambda x: x[1] , reverse=True)
        return [x[0] for x in d[:k]]
        