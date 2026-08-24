class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        op=[]
        for i in range(len(accounts)):
            op.append(sum(accounts[i]))
        op.sort(reverse=True)
        return op[0]
