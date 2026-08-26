class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        k=1
        while True:
            if k in s:
                k+=1
            else: 
                break
        return k