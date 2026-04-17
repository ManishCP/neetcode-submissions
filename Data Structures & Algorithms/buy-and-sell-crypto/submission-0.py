class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        left, right = 0, 1;
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxPro = max(maxPro, profit)
            else:
                left = right
            right+=1
        return maxPro


        