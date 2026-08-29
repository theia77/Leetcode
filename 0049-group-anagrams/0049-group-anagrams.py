class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        L=[]
        group={}
        for i in range(len(strs)):
            dict_i=self.dic(strs[i])
            key = tuple(sorted(self.dic(strs[i]).items()))
            value=strs[i]
            if key in group:
                group[key].append(value)
            else:
                group[key]=[value]
        return list(group.values())

           

    def dic(self,s):
        d={}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        return d