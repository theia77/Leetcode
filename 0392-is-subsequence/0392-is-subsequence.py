class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_1=list(t)
        for i in range(len(s)):
            if(s[i] in t_1):
                t_1.remove(s[i])
        t_2=list(t)
        for x in t_1 :
            if x in t_2:
                t_2.remove(x)
        st="".join(t_2)
        if(st==s):
            return True
        else:
            return False