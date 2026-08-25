class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        x=0
        for i in range (n):
            for j in range(m+x,len(nums1),1):
                nums1[j]=nums2[i]
            x+=1
        nums1.sort()
                
        