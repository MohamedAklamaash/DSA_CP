
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        dp = {}
        def f(ind,buy):
            if ind >= n:
                return 0
            if (ind,buy) in dp:
                return dp[(ind,buy)]
            prof = 0
            if buy:
                op1 = f(ind+1,1)
                op2 = -prices[ind]+f(ind+1,0)
                prof = max(op1,op2)
            else:
                op1 = f(ind+1,0)
                op2 = prices[ind]-fee+f(ind+1,1)
                prof = max(op1,op2)
            dp[(ind,buy)] = prof
            return dp[(ind,buy)]
        return f(0,1)

