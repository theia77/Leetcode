class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]
        s=set(nums1)
        for i in range(len(nums2)):
            if nums2[i] in s:
                l.append(nums2[i])
        return list(set(l))