class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        for x in list(s):
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for x in list(t):
            if x not in d:
                return False
            else:
                d[x]-=1
        for x in d:
            if d[x]!=0:
                return False

        return True