class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l=0
        r=len(people)-1
        boat=0
        while l<=r:
            total=people[l]+people[r]
            if total<=limit:
                boat+=1
                l+=1
                r-=1
            
            elif total>limit:
                boat+=1
                r-=1
        return boat