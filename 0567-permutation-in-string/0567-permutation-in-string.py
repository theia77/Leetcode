class Solution(object): 
    def checkInclusion(self, s1, s2): 
        """ 
        :type s1: str 
        :type s2: str 
        :rtype: bool 
        """ 

        dic_s1 = self.dictionary(s1)
        l = len(s1)

        for i in range(len(s2) - l + 1):
            st = s2[i:i+l]
            dic_st = self.dictionary(st)

            if dic_st == dic_s1:
                return True

        return False

    def dictionary(self, s): 
        d = {}

        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        return d