class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        result = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                max += accounts[i][j]
            if max > result:
                result = max
            max = 0
        return result
