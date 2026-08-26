class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        c_s=0
        for i in range(len(s)):
            if (s[i]==' '):
                c_s+=1
        y_1=0
        y_2=0
        c_p=len(pattern)
        d_1={}
        d_2={}
        p=list(pattern)
        st=s.split()
        if(c_p==c_s+1):
            for i in range(c_p):
                key=p[i]
                value=st[i]
                if key in d_1 and d_1[key]!=st[i]:
                    return False   
                else:
                    d_1[key]=value
            y_1=1
            for j in range(c_p):
                k=st[j]
                v=p[j]
                if k in d_2 and d_2[k]!=p[j]:
                    return False 
                else:
                    d_2[k]=v
            y_2=1
            if(y_1==1 and y_2==1):
                return True
        else:
            return False