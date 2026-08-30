class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mod=10**9+7
        rev=0
        if x>=0:
            rev=int(str(x)[::-1])
            if rev<=pow(2,31)-1:
                return rev
            else:
                return 0
        else:
            sign=-1
            n=abs(x)
            rev=int(str(n)[::-1])
            if rev*sign>=-pow(2,31): 
                return rev*sign
            else:
                return 0
