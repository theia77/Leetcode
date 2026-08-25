class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st=list(s)
        tt=list(t)
        st.sort()
        tt.sort()
        if st==tt:
            return True
        else:
            return False