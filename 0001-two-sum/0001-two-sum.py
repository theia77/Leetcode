class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        newList=[]
        for i in range(len(nums)):
            required=target-nums[i]
            if required in nums[i+1:]:
                newList.append(i)
                newList.append(nums.index(required,i+1))
                return newList
    