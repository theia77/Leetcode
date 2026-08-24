class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=[]
        x=0
        for i in range(len(nums)):
            num.append(nums[i]+x)
            x=x+nums[i]
        return num