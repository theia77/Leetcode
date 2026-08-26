class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st=list(s)
        tt=list(t)
        d_1={}
        d_2={}
        if(len(st)==len(tt)):
            for i in range(len(st)):
                key=st[i]
                value=tt[i]
                if key in d_1 and d_1[key]!=tt[i]:
                    return False
                else:
                    d_1[key]=value
            for j in range(len(tt)):
                k=tt[j]
                val=st[j]
                if k in d_2 and d_2[k]!=st[j]:
                    return False
                else:
                    d_2[k]=val
            return True 
        else:
            return False