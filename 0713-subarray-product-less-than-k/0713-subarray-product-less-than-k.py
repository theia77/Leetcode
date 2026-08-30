class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        r=0
        count=0
        product=1
        for r in range(len(nums)):
            if k<=1:
                return 0
            product*=nums[r]
            while product>=k:
                product//=nums[l]
                l+=1
            count+=+r-l+1
        return count

            