class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        st=""
        for i in range(len(s)):
            if (s[i].isalnum()):
                st=st+s[i]
        r=st[::-1]
        if(r==st):
            return True
        else:
            return False