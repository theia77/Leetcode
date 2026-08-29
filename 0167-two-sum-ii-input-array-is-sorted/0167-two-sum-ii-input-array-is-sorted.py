class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        Li=[]
        l=0
        r=len(numbers)-1
        for i in range(len(numbers)):
            total=numbers[l]+numbers[r]
            if total==target:
                Li.append(l+1)
                Li.append(r+1)
                break
            elif total<target:
                l+=1
            else:
                r-=1
        return Li