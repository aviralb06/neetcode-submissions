class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[]

        if len(prices) ==1:
            return 0
        

        for i in range(len(prices)):
            j= i+1
            while j<len(prices):
                profit.append(prices[j]-prices[i])
                j+=1
                

        result = sorted(profit)

        if result[-1] <= 0:
            return 0

        return result[-1]
        